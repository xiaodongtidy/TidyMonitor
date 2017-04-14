#!/usr/bin/env python
# -*- coding:utf-8 -*-
from service import linux_common


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
        self.group_name = 'LinuxSystem'
        self.services = [
            linux_common.Cpu,
            linux_common.Memory,
            linux_common.FileSystem
        ]
