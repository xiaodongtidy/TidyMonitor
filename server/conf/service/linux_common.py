#!/usr/bin/env python
# -*- coding:utf-8 -*-
from generic import BaseMonitor
from data_handle import average, hit


class Cpu(BaseMonitor):

    def __init__(self):
        super(Cpu, self).__init__()
        self.name = 'Linux CPU'
        self.interval = 60
        self.plugin_name = 'get_cpu_info'
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
