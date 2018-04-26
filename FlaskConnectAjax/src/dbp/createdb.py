# -*- coding: utf-8 -*-
# @Time:    18/04/2018 8:14 PM
# @Author:  Zihao Zhao
# @E-mail:  zz913@nyu.edu

import pymysql.cursors

# configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root')

# create the database named "dbp"
conn.cursor().execute('create database dbp')
