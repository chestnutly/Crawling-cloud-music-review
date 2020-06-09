#!/usr/bin/env python
#-*-coding:UTF-8-*-
'''
===============================
|编写时间：2019年10月5日
|实现功能：爬取网易云所有歌手id并保存到本地
==========================
'''
import requests
from bs4 import BeautifulSoup
import csv
import io
import time
import sys;
reload(sys);
sys.setdefaultencoding("utf8")
import numpy as np
import xlwt
data_file='id.data'
book = xlwt.Workbook() 
filename = 'name.txt'
filename1 = 'id.txt'
artist_name=" "
h=0
from pyExcelerator import * #导入用到的包
w = Workbook() # 创建一个Excel文件
sheet1 = book.add_sheet(u'sheet1',cell_overwrite_ok=True)
def typeof(variate):
    type=None
    if isinstance(variate,int):
        type = "int"
    elif isinstance(variate,str):
        type = "str"
    elif isinstance(variate,float):
        type = "float"
    elif isinstance(variate,list):
        type = "list"
    elif isinstance(variate,tuple):
        type = "tuple"
    elif isinstance(variate,dict):
        type = "dict"
    elif isinstance(variate,set):
        type = "set"
    return type
    print(type)

# 构造函数获取歌手信息
def get_artists(url):
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Connection': 'keep-alive',
             'Cookie': '_iuqxldmzr_=32; _ntes_nnid=0e6e1606eb78758c48c3fc823c6c57dd,1527314455632; '
                       '_ntes_nuid=0e6e1606eb78758c48c3fc823c6c57dd; __utmc=94650624; __utmz=94650624.1527314456.1.1.'
                       'utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=blBrSVohtue8%2B6VgDkxOkJ2G0VyAgyOY;'
                       ' JSESSIONID-WYYY=Du06y%5Csx0ddxxx8n6G6Dwk97Dhy2vuMzYDhQY8D%2BmW3vlbshKsMRxS%2BJYEnvCCh%5CKY'
                       'x2hJ5xhmAy8W%5CT%2BKqwjWnTDaOzhlQj19AuJwMttOIh5T%5C05uByqO%2FWM%2F1ZS9sqjslE2AC8YD7h7Tt0Shufi'
                       '2d077U9tlBepCx048eEImRkXDkr%3A1527321477141; __utma=94650624.1687343966.1527314456.1527314456'
                       '.1527319890.2; __utmb=94650624.3.10.1527319890',
             'Host': 'music.163.com',
             'Referer': 'http://music.163.com/',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html5lib')
    for artist in soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'}):
        artist_name = artist.string
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        
        with open(filename, 'a') as f:
             f.write(artist_name+'\n')
             print("成功储存name"+artist_name)
             time.sleep(0.1)
        with open(filename1, 'a') as h:
             h.write(artist_id+'\n')
             print("成功储存id"+artist_id)
             time.sleep(0.1)


        #try:
          #  writer.writerow((artist_id.decode('utf-8').encode('gbk'), artist_name.decode('utf-8').encode('gbk')))
        #except Exception as msg:
         #   print(msg)


ls1 = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]    # id的值
ls2 = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]    # initial的值
#csvfile = io.open('music_163_artists(1).csv', 'a', encoding='utf-8')    # 文件存储的位置

#writer = csv.writer(csvfile)
#writer.writerow((artist_id.decode('gbk'),artist_name.decode('gbk')))
for i in ls1:
    for j in ls2:
        url = 'http://music.163.com/discover/artist/cat?id=' + str(i) + '&initial=' + str(j)
        get_artists(url)
