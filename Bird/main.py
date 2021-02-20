#!/usr/bin/ python
# -*- coding:utf-8 -*-

import sys
import Setting

from API.Bird_Requests import Bird_Requests
from API.Bird_stastic import wordcloud_create, FILE_NAME
from API.Filter import num_count

if __name__ == '__main__':
    record_url = 'http://www.birdreport.cn:8080/front/record/search/page'
    if sys.argv[1] == '-r' or '-record':
        requests_data = Bird_Requests().requests_bird(url=record_url)
        tuple1 = [(k, v) for k, v in num_count(requests_data).items()]
        wordcloud_create(tuple1)
        if Setting.HTML_TO_IMAGE:
            from API.Html_to_photo import turn_to_image

            turn_to_image(FILE_NAME, FILE_NAME.split('.') + '.png')
        else:
            pass
        print('Finish!')
        sys.exit()
    else:
        print("""
        usage:
            '-r' or '-record'  To get the record of birdreport
        """)