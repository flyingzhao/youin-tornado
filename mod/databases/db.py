# -*- coding: utf-8 -*-
DB_HOST = '115.28.27.150'
# DB_HOST = '127.0.0.1'
DB_USER = 'youyinuser'
# DB_USER = 'root'
DB_PWD = 'youyin2015'
# DB_PWD = '084358'
DB_NAME = 'youyin'


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() #create Base lei
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                     encoding='utf-8', echo=False,
                       pool_size=100, pool_recycle=10)
