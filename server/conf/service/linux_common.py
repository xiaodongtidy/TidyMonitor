#!/usr/bin/env python
# -*- coding:utf-8 -*-
from generic import BaseMonitor
from data_handle import average, hit


class Cpu(BaseMonitor):

    def __init__(self):
        super(Cpu, self).__init__()
        self.name = 'Linux CPU'
        self.interval = 60
        self.plugin_name = 'cpu'
        self.triggers = {
            'idle': {'func': average,
                     'minute': 15,
                     'compare': 'lt',
                     'warning': 30,
                     'critical': 15,
                     'data_type': 'percentage'},
            'iowait': {'func': hit,
                       'minute': 20,
                       'compare': 'gt',
                       'warning': 40,
                       'critical': 75,
                       'threshold': 4,
                       'data_type': 'percentage'}
        }


class Memory(BaseMonitor):

    def __init__(self):
        super(Memory, self).__init__()
        self.name = 'Linux Memory'
        self.interval = 120
        self.plugin_name = 'memory'
        self.triggers = {
            'free': {'func': average,
                     'minute': 10,
                     'compare': 'lt',
                     'warning': 20,
                     'critical': 10,
                     'data_type': 'percentage'}
        }


class FileSystem(BaseMonitor):

    def __init__(self):
        super(FileSystem, self).__init__()
        self.name = 'Disk usage'
        self.interval = 300
        self.plugin_name = 'file_system'
        self.triggers = {
            'used': {'func': hit,
                     'minute': 20,
                     'compare': 'lt',
                     'warning': 25,
                     'critical': 15,
                     'data_type': 'percentage'}
        }
