#!/usr/bin/env python
# -*- coding:utf-8 -*-
import global_settings
from redis_helper import RedisHelper


class MonitorServer(object):

    def __init__(self):
        self.redis = RedisHelper()

    def handle(self):
        pass

    def run(self):
        pass
