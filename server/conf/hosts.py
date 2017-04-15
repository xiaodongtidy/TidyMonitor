#!/usr/bin/env python
# -*- coding:utf-8 -*-
import template

g1 = template.LinuxCommonTemplate()
g1.group_name = 'All hosts'
g1.hosts = ['192.168.40.157', '192.168.40.135']

g2 = template.WebServiceTemplate()
g2.group_name = 'Web hosts'
g2.hosts = ['192.168.40.157']

monitor_hosts = [g1, g2]
