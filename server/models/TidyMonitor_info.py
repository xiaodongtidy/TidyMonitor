#!/usr/bin/env python
# -*- coding:utf-8 -*-
from server.utility.mysql_helper import MysqlHelper


class TidyMonitorInfo(object):

    def __init__(self):
        self.mysql = MysqlHelper()

    def select_time_stamp(self, ip, service_name):
        sql = "select time_stamp from TidyMonitor_info where ip=%s and service_name=%s order by id desc limit 1"
        params = (ip, service_name)
        return self.mysql.get(sql, params)

    def insert_monitor_info(self, ip, service_name, info_data, time_stamp):
        sql = "insert into TidyMonitor_info (ip, service_name, info_data, time_stamp) values (%s, %s, %s, %s)"
        params = (ip, service_name, info_data, time_stamp)
        return self.mysql.insert(sql, params)
