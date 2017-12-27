#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
任务 发送邮件
"""

from app import celery

# email
from flask_mail import Message
from app import mail


@celery.task(name='send_email')
def send_async_email(touser):
    """ Background task to send an email with Flask-Mail."""
    # send the email
    msg = Message('Hello from Flask', recipients=[touser])  # recipients 收件人
    msg.body = 'This is a test email sent from a background Celery task.'
    with app.app_context():
        mail.send(msg)
