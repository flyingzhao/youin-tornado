#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey, Float 
from sqlalchemy.orm import relationship,backref
from db import engine,Base

class User(Base):
	__tablename__ = 'Users'

	uid = Column(VARCHAR(64),primary_key=True)
	name = Column(VARCHAR(64))
	email = Column(VARCHAR(64))
	phone = Column(VARCHAR(64),index=True,nullable=False)
	gender = Column(VARCHAR(64))
	password = Column(VARCHAR(64))
	salt = Column(VARCHAR(64))
	school = Column(VARCHAR(64),default=u'东南大学')
	picture = Column(VARCHAR(64),default='/static/images/pic/default_pic.jpg')




class Cookie(Base):
	__tablename__ = "Cookie"

	id = Column(Integer,primary_key=True)
	uid = Column(VARCHAR(64),ForeignKey('Users.uid', ondelete='CASCADE'))
	cookie = Column(VARCHAR(64))

class PhoneCode(Base):
	__tablename__ = "PhoneCode"

	id = Column(Integer,primary_key=True)
	phone = Column(VARCHAR(11),ForeignKey('Users.phone',ondelete='CASCADE'))
	code = Column(VARCHAR(6),nullable=False)
	time = Column(VARCHAR(15),nullable=False)
	count = Column(Integer,default=0)