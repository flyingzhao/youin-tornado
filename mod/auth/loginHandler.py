# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
from ..databases.tables import User,Cookie
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
import uuid,re
from time import time
import traceback
import uuid
from ..Basehandler import BaseHandler
import hashlib,random,string

class LoginHandler(BaseHandler):
    def get(self):
        """
            可以渲染登录页面，也可以不用
        """

    def post(self):
        """
        用户登录，成功则返回200，并且设置cookie
        参数：
            phone
            password
        返回：
        """
        retjson = {'code':200,'content':u'登录成功'}
        try:
            arg_phone = self.get_argument('phone')
            arg_password = self.get_argument('password')
            if not arg_phone:
                retjson['code'] = 400
                retjson['content'] = u'参数不能为空'
            elif len(arg_password) < 6:
                retjson['code'] = 400
                retjson['content'] = u'密码太短'
            else:
                try:
                    person = self.db.query(User).filter(User.phone==arg_phone).one()
                    passwd = hashlib.md5(person.salt.join(arg_password)).hexdigest()
                    if passwd == person.password:
                        cookie_uuid=uuid.uuid1()
                        self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+2592000)
                        status = Cookie(cookie=cookie_uuid,uid=person.uid)
                        self.db.add(status)
                        try:
                            self.db.commit()
                        except Exception,e:
                            retjson['code'] = 500
                            retjson['content'] = u'cookie存储错误'
                            self.db.rollback()
                    else:
                        retjson['code'] = 401
                        retjson['content'] = u'密码错误'
                except NoResultFound:
                    retjson['code'] = 403
                    retjson['content'] = u'用户不存在'
        except Exception,e:
            print str(e)
            retjson['code'] = 400
            retjson['content'] = u'参数太少'

        self.write(json.dumps(retjson,ensure_ascii=False, indent=2))
        self.finish() 

    def delete(self):
        """
        删除用户：
            根据cookie删除用户

        """
        retjson = {'code':200,'content':u'删除成功'}
        try:
            current_cookie = self.current_user
            if current_cookie:
                current_user = self.db.query(User).filter(User.uid==current_cookie.uid).one()
                self.db.delete(current_user)
                try:
                    self.db.commit()
                except Exception,e:
                    print str(e)
                    self.db.rollback()
                    retjson['code'] = 500
                    retjson['content'] = u'系统错误'
            else:
                retjson['code'] = 403
                retjson['content'] = u'请先登录'
        except NoResultFound:
            retjson['code'] = 403
            retjson['content'] = u'用户不存在'
        except Exception,e:
            print str(e)
            retjson['code'] = 500
            retjson['content'] = u'系统错误'
        self.write(json.dumps(retjson,ensure_ascii=False, indent=2))
        self.finish() 
