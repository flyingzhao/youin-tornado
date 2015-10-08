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

class RegisterHandler(BaseHandler):


    def get(self):
        """
            可以是注册页面
            也可以不用
        """
        pass

    """
    post函数:
        接受传过来的注册参数，
        注册成功返回成功，code为200

        参数：
            name:
            phone:
            email:
            password:
        返回：
            {'code':200,'content':'ok'}

    
    """
    def post(self):
        retjson = {'code':200,'content':'ok'}
        try:
            arg_name = self.get_argument('name')
            arg_phone = self.get_argument('phone')
            arg_email = self.get_argument('email')
            arg_password = self.get_argument('password')
            if not arg_name or not arg_phone or not arg_email:
                retjson['code'] = 400
                retjson['content'] = u'参数不能为空'
            elif re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", arg_email) == None :
                retjson['code'] = 402
                retjson['content'] = u'邮箱格式不对'
            elif len(arg_password) < 6:
                retjson['code'] = 400
                retjson['content'] = u'密码太短'
            else:
                status = 1
                uid_uuid = ''
                try:
                    uid_uuid = uuid.uuid5(uuid.NAMESPACE_DNS,'youyin'+str(arg_phone))
                    salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
                    arg_password = hashlib.md5(salt.join(arg_password)).hexdigest()
                    user = User(uid = uid_uuid,email = arg_email,phone = arg_phone,name = arg_name,password = arg_password,salt = salt)
                    self.db.add(user)
                    self.db.commit()
                except IntegrityError,e:
                    status = 0
                    retjson['code'] = 402
                    retjson['content'] = u'该手机号已被注册'
                    self.db.rollback()
                except Exception,e:
                    status = 0
                    retjson['code'] = 500
                    retjson['content'] = u'系统错误'
                    print str(e)
                    self.db.rollback()
                if status==1:
                    try:
                        print 'get'
                        cookie_uuid=uuid.uuid1()
                        status_cookie = Cookie(cookie=cookie_uuid,uid=uid_uuid)
                        self.db.add(status_cookie)
                        self.db.commit()
                        self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+2592000)
                    except Exception,e:
                        retjson['code'] = 500
                        retjson['content'] = u'cookie存储错误'
                        self.db.rollback()
        except Exception,e:
            print str(e)
            retjson['code'] = 400
            retjson['content'] = u'参数太少'
        self.write(json.dumps(retjson,ensure_ascii=False, indent=2))
        self.finish()

    


