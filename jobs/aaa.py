#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
任务
"""

from app import celery


@celery.task(name='aaaa')
def aaaa(a, b):
    print('Hello job aaaa')
    return a + b


@celery.task(name='bbbb')
def bbbb(a, b):
    print('Hello job bbbb')
    print(a + b)
    return a + b
