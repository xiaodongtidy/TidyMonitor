#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cpu
import memory
import nginx
import php
import mysql


def run_plugins(plugin_name):
    return plugin_name.monitor()
