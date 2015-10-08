# -*- coding: utf-8 -*-
#!/usr/bin/env python
from ..Base_Handler import BaseHandler
from ..databases.tables import Cookie
#/auth/logout
class LogoutHandler(BaseHandler):
    # @tornado.web.authenticated
    def delete(self):#用户登出，删除cookie
        status = self.current_user
        if status:
            self.db.delete(status)
            try:
                self.db.commit()
            except Exception,e:
                self.db.rollback()
        else:
            pass