#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import engine, Base
from tables import User,Cookie,PhoneCode
try:
    Base.metadata.create_all(engine) #create all of Class which belonged to Base Class
except Exception,e:
    print str(e)