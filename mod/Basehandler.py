# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from databases.tables import Cookie
from sqlalchemy.orm.exc import NoResultFound

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    def on_finish(self):
        self.db.close()
    def get_current_user(self):
        name = self.get_secure_cookie("username")
        if name:
            try:
                status = self.db.query(Cookie).filter(Cookie.cookie == name).one()
                return status
            except NoResultFound:
                return False
        else:
            return False