#!/usr/bin/env python
# -*- coding:utf-8 -*-
import global_settings
import pickle
import function_packages
from redis_helper import RedisHelper


class MonitorServer(object):

    def __init__(self):
        self.redis = RedisHelper()

    def handle(self):
        redis_sub = self.redis.subscribe()
        while True:
            msg = redis_sub.parse_response()
            # 根据返回的消息头，执行消息头所对应的方法
            msg_client = pickle.loads(msg[2])
            func_name = msg_client.keys()[0]
            func = getattr(function_packages, func_name)
            func(msg_client[func_name])

            # 处理刚接收的数据
            pass

    def run(self):
        print '--- start to monitor host ---'
        self.handle()

if __name__ == '__main__':
    s = MonitorServer()
    s.run()
