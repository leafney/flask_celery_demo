#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
任务 通过 add_periodic_task 添加异步任务
"""

from app import celery
from celery.schedules import crontab


@celery.task(name='periodic')
def test(a, b):
    """通过代码添加定时任务"""
    c = a + b
    print('periodic job test')
    return c


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s(1, 2), name='periodic')

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )
