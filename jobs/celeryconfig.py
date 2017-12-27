#!/usr/bin/env python3
# -*- coding: utf-8 -*-

broker_url = 'redis://192.168.5.123:6379/1'
result_backend = 'redis://192.168.5.123:6379/2'

# import
imports = ('jobs.tasks', 'jobs.email')

# # 任务序列化和反序列化使用msgpack方案
# task_serializer = 'msgpack'
# # 读取任务结果使用json
# result_serializer = 'json'
# # 指定接受的内容类型
# accept_content = ['json', 'msgpack']
timezone = 'Asia/Shanghai'
enable_utc = True


# beat schedules
from datetime import timedelta

beat_schedule = {
    'printy': {
        'task': 'printy',
        'schedule': timedelta(seconds=5),  # 每 5 秒执行一次
        'args': (8, 2)
    }
}
