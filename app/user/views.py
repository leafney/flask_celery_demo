#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, current_app
from flask import flash, request, redirect, url_for

from . import user


@user.route('/')
def home():
    return "This is User Home Page"
