#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
from hashlib import sha256

def hash_password(password, salt='lizhenlong'):
    """简单的加密密码的HASH算法，SHA256加密，固定加salt，三轮HASH"""
    result = str(password) + salt
    for i in range(3):
        result = sha256(result.encode(encoding='UTF-8')).hexdigest()
    return result
