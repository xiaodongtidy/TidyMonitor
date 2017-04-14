#!/usr/bin/env python
# -*- coding:utf-8 -*-
from generic import BaseMonitor
from data_handle import hit


class Nginx(BaseMonitor):

    def __init__(self):
        super(Nginx, self).__init__()
        self.name = 'Middleware nginx'
        self.interval = 60
        self.plugin_name = 'get_nginx_info'
        self.triggers = {
            'alive': {'func': hit,
                      'minute': 5,
                      'compare': 'gt',
                      'warning': 1,
                      'critical': 1,
                      'threshold': 1,
                      'data_type': 'boolean'
                      }
        }
