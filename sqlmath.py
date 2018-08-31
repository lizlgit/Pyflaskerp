#!/usr/bin/env python3
# -*- coding=utf8 -*-
#from dblink import db
from shapasswd import hash_password
from setting import User,Goods,Good_model,Good_supplier,Good_log,db
import datetime
#定义函数去使用ORM
def add_user(u1,u2,u3,u4,u5):
    u0 = User(user=u1, code=u2,password=str(hash_password(u3)),telephone = u4,create_time = datetime.datetime.now(), sts = u5)
    db.session.add(u0)
    db.session.commit()

def add_supplier(s1,s2,s3,s4,s5,s6,s7):
    s0 = Good_supplier(supplier=s1,short_name=s2,linkman=s3,telephone=s4,address=s5,other=s6,sts=s7)
    db.session.add(s0)
    db.session.commit()

def mima(usercode,password):
    s0 = User.query.filter(User.code==usercode ).first()
    s1 = s0.password
    s2 = hash_password(password)
    if s0 == None:
        return 'ERROR'
    elif s1 == s2:
        return usercode
    else:
        return 'ERROR'
