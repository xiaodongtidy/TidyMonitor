#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis


class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.40.135')
        self.chan_sub = 'fm101'
        self.chan_pub = 'fm101'

    def set(self, key, value):
        self.__conn.set(key, value)

    def get(self, key):
        return self.__conn.get(key)

    def publish(self, msg):
        self.__conn.publish(self.chan_pub, msg)

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
