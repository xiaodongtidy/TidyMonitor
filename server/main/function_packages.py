#!/usr/bin/env python
# -*- coding:utf-8 -*-
import global_settings
import pickle
import time
from redis_helper import RedisHelper
from server.conf import hosts


def flush_all_host_configs_into_redis():
    apply_host = []
    # 取出需要配置的ip
    for group in hosts.monitor_hosts:
        apply_host.extend(group.hosts)
    # 去重复客户端ip
    apply_host = set(apply_host)
    redis = RedisHelper()
    for client_ip in apply_host:
        # 通过ip取出模板中的监控配置
        apply_configs = host_config_handle(client_ip)
        key = 'HostConfig:%s' % client_ip
        redis.set(key, pickle.dumps(apply_configs))
    return True


def host_config_handle(client_ip):
    config_services = []
    configs = {}
    for group in hosts.monitor_hosts:
        if client_ip in group.hosts:
            # 取出一个ip下所有的监控配置
            config_services.extend(group.services)
    config_services = set(config_services)

    for service in config_services:
        service = service()
        configs[service.name] = [service.interval,
                                 service.plugin_name,
                                 service.last_time
                                 ]
    return configs


def report(msg):
    msg_client = pickle.loads(msg)
    client_ip = msg_client['ip']
    key = 'StatusData:%s' % client_ip
    msg_client['time_stamp'] = time.time()
    redis = RedisHelper()
    redis.set(key, pickle.dumps(msg_client))
