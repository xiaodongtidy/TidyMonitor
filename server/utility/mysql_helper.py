#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import conf.config


class MysqlHelper(object):

    def __init__(self):
        self.__conn_dict = server.conf.config.conn

    def get(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def insert(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return True

    def update(self, sql):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return True

    def get_all(self, sql):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
