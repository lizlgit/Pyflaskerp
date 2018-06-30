#!/usr/bin/env python3
# -*- coding=utf8 -*-
#导入数据库工具，这个是支持Python3的
import pymysql
#定义数据库连接
def db(table):
    conn = pymysql.connect(
        host='139.199.80.151', port=3306,
        user='root', passwd='lzl@233233',
        db='flaskerp', charset='utf8',
    )
    cur = conn.cursor()
    res = cur.execute(table)
    res = cur.fetchmany(res)
    cur.close()
    conn.commit()
    conn.close()
    return res
