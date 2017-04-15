#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BaseMonitor(object):

    def __init__(self):
        self.name = 'BaseMonitor'
        self.interval = 300
        self.last_time = 0
        self.plugin_name = 'Your plugin name'
        self.triggers = {}
