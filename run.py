#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')