#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cpu_plugin
import memory_plugin
import nginx_plugin
import php_plugin
import mysql_plugin
import file_system_plugin


def cpu():
    return cpu_plugin.monitor()


def memory():
    return memory_plugin.monitor()


def nginx():
    return nginx_plugin.monitor()


def php():
    return php_plugin.monitor()


def mysql():
    return mysql_plugin.monitor()


def file_system():
    return file_system_plugin.monitor()
