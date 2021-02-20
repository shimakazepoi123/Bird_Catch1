#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json


def check_if_none():
    with open('config.json', 'r+') as file1:
        data = json.load(file1)
        if len(data['page']) < 1 or len(data['limit']) < 1:
            raise Exception('page值或limit值不能为空')
        else:
            return data
