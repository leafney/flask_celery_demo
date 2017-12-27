#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
任务 添加需要导入current_app的任务
"""

from app import celery

# email
from flask_mail import Message
from app import mail
from flask import current_app


@celery.task(name='send_email')
def send_async_email(touser):
    """ Background task to send an email with Flask-Mail."""
    app = current_app._get_current_object()
    # send the email
    msg = Message('Hello from Flask', recipients=[touser])  # recipients 收件人
    msg.body = 'This is a test email sent from a background Celery task.'
    with app.app_context():
        mail.send(msg)
