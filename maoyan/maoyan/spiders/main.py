# -*- coding: utf-8 -*-
"""
@Time   : 2018/9/17 16:31
@File   : main.py
@Author : ZZShi
程序作用：

"""
from scrapy import cmdline


cmdline.execute('scrapy crawl comment'.split())
