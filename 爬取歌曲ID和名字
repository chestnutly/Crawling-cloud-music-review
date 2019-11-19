#!/usr/bin/env python
#-*-coding:UTF-8-*-

'''
===============================
|编写时间：2019年9月27日
|实现功能：爬取网易云的所有歌曲id与名字
==========================
'''
import requests
import json
import time
import io
import sys
from bs4 import BeautifulSoup
import requests
import random
from lxml import etree
reload(sys) 
sys.setdefaultencoding('utf-8')
songs_name=[]
arist_list=[]
filename= r'result-artistid.txt'
with open(filename,'r') as f:
    artist_list = list(f)

class GetComments(object):
    def __init__(self):
        self.headers = {
            'Referer': 'http://music.163.com/',
            'Host': 'music.163.com',
            'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/x-www-form-urlencoded",
            'Origin': 'https://music.163.com',
            'Connection': "keep-alive",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        # 构造会话
        self.session = requests.session()
        # 设置代理
        self.proxies = {
            'http': 'http://183.62.22.220:3128',
            'http': 'http://118.190.95.35:9001',
            'http': 'http://61.135.217.7:80',
            'http': 'http://106.75.9.39:8080',
            'http': 'http://118.190.95.43:9001',
            'http': 'http://121.31.157.94:8123',
            'http': 'http://115.46.67.248:8123',
            'http': 'http://182.88.14.243:8123'
        }

    def get_json(self, song_id, offset):
        """
        获取json数据
        :param song_id: 歌曲id
        :param offset: 评论偏移量
        :return: json转成的dict
        """
        url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_%s?limit=20&offset=%s' % (song_id, offset)
        print(url)
        responses = self.session.get(url, headers=self.headers).content
        json_dict = json.loads(responses)
        return json_dict

    def save_data(self, comments, song_name):
        """
         保存数据
        :param comments: 保存评论的列表
        :param song_name: 歌曲名字
        :return:
        """
        #从unicode转换为utf-8
        hear = str(comments).replace('u\'','\'')
        print hear.decode("unicode-escape")

    def get_songs_id(self, url):
        """
        :param url: 主页链接
        :return: 所有歌曲名字，id
        """
        html = self.session.get(url, headers=self.headers)
        text = etree.HTML(html.text)
        # print(html.text)
        songs_name = text.xpath('//div[@id="hotsong-list"]/div[@class="f-cb"]/div/ul//a/text()')
        songs_id = text.xpath('//div[@id="hotsong-list"]/div[@class="f-cb"]/div/ul//a/@href') # 获取歌曲id
        songs_id = [s_id[9:] for s_id in songs_id]
        print(str(songs_name))
        print("已经爬取到歌手id:")
        print(str(id))
        filename = 'songid.txt'
        songname='songname.txt'
        with open(filename, 'a') as f:
            for line in songs_id:
                f.write(line+'\n')
        with open(songname, 'a') as h:
            for line in songs_name:
                h.write(line+'\n')
            
        


if __name__ == '__main__':
       for i in range(len(artist_list)):
           id=int(artist_list[i])
           singer_url = 'https://music.163.com/artist?id='+str(id) # 复制网址时记得要去掉网址的#号
           spider = GetComments()
           spider.get_songs_id(singer_url)
           time.sleep(0.1)
