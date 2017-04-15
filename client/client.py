#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import pickle
import time
from redis_helper import RedisHelper
from plugins import plugins_api
client_ip = '192.168.40.135'


class MonitorClient(object):

    def __init__(self):
        self.redis = RedisHelper()
        self.configs = {}

    @staticmethod
    def format_msg(key, value):
        msg = {key: value}
        return pickle.dumps(msg)

    def get_configs(self):
        configs = self.redis.get('HostConfig:%s' % client_ip)
        if configs:
            self.configs = pickle.loads(configs)
        return True

    def handle(self):
        if self.get_configs():
            while True:
                for service_name, config_value in self.configs.items():
                    interval, plugin, last_time = config_value
                    if time.time() - last_time > interval:
                        a = threading.Thread(target=self.task, args=[service_name, plugin])
                        a.start()
                        self.configs[service_name][2] = time.time()
                    else:
                        wait_time = interval - (time.time() - last_time)
                        print 'please wait %s seconds' % wait_time
                time.sleep(1)
        else:
            print '--- could not find the monitor configure ---'

    def task(self, service_name, plugin_name):
        print '--- Going to handle the %s task ---' % service_name
        func = getattr(plugins_api, plugin_name)
        res = func()
        print "\033[1;32m%s\033[0m" % res
        # 拼接出传递的数据
        msg = self.format_msg('report',
                              {'ip': client_ip,
                               'service_name': service_name,
                               'info_data': res
                               })
        self.redis.publish(msg)

    def run(self):
        print '--- start Monitor Client ---'
        self.handle()

if __name__ == '__main__':
    c = MonitorClient()
    c.run()
