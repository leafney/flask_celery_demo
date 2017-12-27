#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
flask配置文件
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'guess'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig"""
    DEBUG = True
    AAA = 'this is DevelopmentConfig'
    # email
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'flask@163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False


class TestingConfig(Config):
    """docstring for TestingConfig"""
    TESTING = True
    AAA = 'this is TestingConfig'


class ProductionConfig(Config):
    """docstring for ProductionConfig"""
    AAA = 'this is ProductionConfig'
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
