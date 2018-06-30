#!/usr/bin/env python3
# -*- coding=utf8 -*-
#导入数据库工具，这个是支持Python3的
from dblink import db
#定义数据库连接

def fordata(fordata,type):
    if type == 1 :
        s1 = 'select g.g_code as a ,gm.good_name as b ,gm.model_number as c ,gm.color as d ,g.man_user as e ,g.status  as f from goods as g left join good_model as gm on g.gm_code=gm.gm_code where status=1'
        ress = db(s1)
        return ress
    elif type == 2 :
        s2 = 'select * from {0} where sts=1'.format(fordata)
        ress = db(s2)
        return ress
    elif type == 3 :
        s3 = 'select * from {0} where sts=1'.format(fordata)
        ress = db(s3)
        return ress
    elif type == 4 :
        s4 = 'select * from {0} where sts=1'.format(fordata)
        ress = db(s4)
        return ress
    else :
        return None
# 定义最简单的登录验证
def logindata(username,password):
    s1 = "select password from user where code='{0}'".format(username)
    ress = str(db(s1))
    if ress == password:
        return True
    else:
        return False
