#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from config import config
# celery
from celery import Celery
# email
from flask_mail import Mail, Message


celery = Celery(__name__)
celery.config_from_object('jobs.celeryconfig')


mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)

    # 附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app
