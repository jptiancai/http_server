#!/usr/bin/env bash
# -*- coding:utf-8 -*-
mkdir -p logs

python server.py >./logs/start.log 2>&1
