#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
===============================
|编写时间：2019年9月25日
|实现功能：爬取网易云的热评
==========================
'''
import io
import os
import requests
import json
from bs4 import BeautifulSoup
import time
import sys
import importlib

importlib.reload(sys)
id_list = []
content = {}
x = 0
path = r'/home/leo/Desktop/cloudMusicSpider/获取网易云全部热评/html文件'
filename = r'wangyiyunhot.txt'
songname_filename = r'songname.txt'
with open('songid.txt', 'r') as f:
    id_list = list(f)
with open('songname.txt', 'r') as k:
    name_list = list(k)

class hotComments:
    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        }

    # offset页数,limit一页显示最多的评论数
    def get_hotComments(self, music_id):
        global x
        self.url = "http://music.163.com/api/v1/resource/comments/R_SO_4_{}?offset=0&limit=50".format(music_id)
        print(self.url)
        try:
            self.text = json.loads(requests.get(self.url, headers=self.headers).text)
            datas = self.text['hotComments']
            for content in datas:
                with io.open(filename, 'a', encoding='utf-8') as f:
                    f.write(content['content'] + "\r\n")
                    os.chdir(path)
                    filename2 = str(x) + '.html'
                with open(filename2, 'a') as f:
                    f.write("<div  class='title'> " + str(name_list[i]).replace("\n", " ") + "</div>" + "\r\n")
                    f.write("<div  class='context'> " + str(content['content']) + "</div>" + "\r\n")
                    x = x + 1
                    f.close()
            print("已经爬取到歌曲： id" + str(id))
        except Exception as msg:
            print(msg)
            print("爬取失败！！！" + str(id))
            sys.exit(0)

if __name__ == '__main__':
    for i in range(len(id_list)):
        music = hotComments()
        id = int(id_list[i])
        music.get_hotComments(id)
        print("爬取的次数：" + str(i))
        time.sleep(0.1)
