#!/usr/bin/env python
# -*- coding:utf-8 -*-
from service import linux_common
from service import nginx
from service import php
from service import mysql


class BaseTemplate(object):

    def __init__(self):
        self.name = 'Your template name'
        self.group_name = 'Your group name'
        self.hosts = []
        self.services = []


class LinuxCommonTemplate(BaseTemplate):

    def __init__(self):
        super(LinuxCommonTemplate, self).__init__()
        self.name = 'LinuxCommonTemplate'
        self.services = [
            linux_common.Cpu,
            linux_common.Memory,
            linux_common.FileSystem
        ]


class WebServiceTemplate(BaseTemplate):

    def __init__(self):
        super(WebServiceTemplate, self).__init__()
        self.name = 'WebServiceTemplate'
        self.services = [
            nginx.Nginx,
            php.PhpFpm,
        ]


class MysqlTemplate(BaseTemplate):

    def __init__(self):
        super(MysqlTemplate, self).__init__()
        self.name = 'MysqlTemplate'
        self.services = [
            mysql.Mysql
        ]
