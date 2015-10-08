# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options

from sqlalchemy.orm import scoped_session, sessionmaker
from mod.databases.db import engine



from mod.auth.registerHandler import RegisterHandler
from mod.auth.loginHandler import LoginHandler

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/youin/auth/reg',RegisterHandler),
            (r'/youin/auth/login',LoginHandler)
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True
        )

        tornado.web.Application.__init__(self, handlers,**settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')
        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
