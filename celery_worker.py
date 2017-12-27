#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import create_app, celery

app = create_app('default')
app.app_context().push()
