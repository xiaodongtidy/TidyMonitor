#!/usr/bin/env python
# -*- coding:utf-8 -*-
from generic import BaseMonitor
from data_handle import hit


class Mysql(BaseMonitor):

    def __init__(self):
        super(Mysql, self).__init__()
        self.name = 'Middleware mysql'
        self.interval = 60
        self.plugin_name = 'mysql'
        self.triggers = {
            'alive': {'func': hit,
                      'minute': 5,
                      'compare': 'eq',
                      'warning': True,
                      'critical': True,
                      'threshold': 1,
                      'data_type': 'boolean'
                      },
            'connect': {'func': hit,
                        'minute': 5,
                        'compare': 'gt',
                        'warning': 140,
                        'critical': 190,
                        'threshold': 4,
                        'data_type': 'times'
                        }
        }
