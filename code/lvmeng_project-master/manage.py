#!/usr/bin/env python
#coding:utf-8
import os
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
