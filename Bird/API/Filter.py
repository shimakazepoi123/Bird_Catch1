#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter


def num_count(stastic: dict):
    dict1 = Counter([i['taxon_name'] for i in stastic['data']])
    return dict1


def filter1(num_dict: dict, num: int):
    for i, k in list(num_dict.items()):
        if k < num:
            del num_dict[i]
        else:
            pass
    tuple1 = [(k, v) for k, v in num_dict.items()]
    return tuple1
