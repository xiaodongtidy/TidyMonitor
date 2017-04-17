#!/usr/bin/env python
# -*- coding:utf-8 -*-
import global_settings
import pickle
import function_packages
import threading
import time
from utility.redis_helper import RedisHelper
from models.TidyMonitor_info import TidyMonitorInfo


class MonitorServer(object):

    def __init__(self):
        self.redis = RedisHelper()
        self.TidyMonitorInfo = TidyMonitorInfo()
        self.configs = {}

    def monitor(self):
        apply_host = function_packages.get_apply_host()
        while True:
            for client_ip in apply_host:
                apply_configs = function_packages.host_config_handle(client_ip)
                for service_name, config_value in apply_configs.items():
                    interval, plugin, last_time = config_value
                    time_stamp = self.TidyMonitorInfo.select_time_stamp(client_ip, service_name)
                    tim = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    if time_stamp:
                        data_time = time_stamp[0]['time_stamp']
                        if time.time() - data_time < interval:
                            print "--- %s [ip]%s: %s is running ---" % (tim, client_ip, service_name)
                        else:
                            print "--- %s [ip] %s: %s is uncommitted overtime ---" % (tim, client_ip, service_name)
                    else:
                        print "--- %s [ip] %s: %s has not data ---" % (tim, client_ip, service_name)
                time.sleep(1)
            time.sleep(1)

    def handle(self):
        redis_sub = self.redis.subscribe()
        while True:
            msg = redis_sub.parse_response()
            # 根据返回的消息头，执行消息头所对应的方法
            msg_client = pickle.loads(msg[2])
            # print 'recv:', msg_client
            func_name = msg_client.keys()[0]
            client_ip = msg_client.values()[0]['ip']
            func = getattr(function_packages, func_name)
            func(msg_client[func_name])

            # 处理刚接收的数据
            key = 'StatusData:%s' % client_ip
            data = pickle.loads(self.redis.get(key))
            print data
            ip = data.get('ip')
            service_name = data.get('service_name')
            info_data = data.get('info_data')
            time_stamp = data.get('time_stamp')
            res = self.TidyMonitorInfo.insert_monitor_info(ip, service_name, info_data, time_stamp)
            if res is True:
                pass
            else:
                print res

    def run(self):
        print '--- start to monitor host ---'
        a = threading.Thread(target=self.handle, args=[])
        a.start()
        b = threading.Thread(target=self.monitor, args=[])
        b.start()

if __name__ == '__main__':
    s = MonitorServer()
    s.run()
