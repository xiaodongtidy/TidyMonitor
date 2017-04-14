#!/usr/bin/env python
# -*- coding:utf-8 -*-
from generic import BaseMonitor
from data_handle import average, hit


class PhpFpm(BaseMonitor):

    def __init__(self):
        super(PhpFpm, self).__init__()
        self.name = 'Middleware php-fpm'
        self.interval = 60
        self.plugin_name = 'get_php_fpm_info'
        self.triggers = {
            'alive': {'func': hit,
                      'minute': 5,
                      'compare': 'eq',
                      'warning': True,
                      'critical': True,
                      'threshold': 1,
                      'data_type': 'boolean'
                      },
            'slow': {'func': average,
                     'minute': 10,
                     'compare': 'gt',
                     'warning': 5,
                     'critical': 15,
                     'data_type': 'seconds'
                     }
        }
