import json
#import re
import os
import requests
import urllib.request #获取文件
from urllib.parse import urlparse #获取文件名
from pathlib import Path #获取文件类型

def getSource(numSource=None):# numSource 下载源编号,如不填写则默认使用一号下载源
        with open('config.json', 'r') as f: # 读取配置文件,获取默认下载源
            config = json.load(f)
            try:
                if int(numSource) == int(f"{config['downSource']}"):    
                   downSource = f"{config['downSource']}"
                else:
                    downSource = int(numSource)
            except:
                downSource = '1'
        with open('data/downSource.json', 'r') as f: # 读取下载源文件
            data = json.load(f)
            for item in data:
                if item['number'] == int(downSource):#如果item内number（下载源编号）与downSource相同，则返回该item
                    return item
 
# 获取文件列表
def getList(url):
        try:
            response = requests.get(url, timeout=(10,15))
            response.encoding = 'utf-8'
        except:
            print('无法获取文件列表，请检查网络连接以及服务器地址是否正确。')
            return
        
        parsed_url = urlparse(url)
        filename = parsed_url.path.split('/')[-1]
        if filename == 'versions.json':
            filename = 'filelist.json'
        directory = './data/' + filename
        #print(os.path.abspath(directory))

        try:
            content = response.text
            if content == '404 Not Found':
                print('获取文件列表失败，请检查文件列表是否存在以及服务器状态。')

            with open(directory, 'w') as file:
                file.write(content)
                print(f'文件列表已成功保存到 {directory}')
        except:
            print('获取文件列表失败，请检查网络连接以及服务器状态。')
            return
        
# 下载usf最新版
def getusf(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        list = json.load(file)
    
    #print('最新版本' + list[0]['name'])
    url = 'https://usfdown.zuyst.top' + list[0]['downloadLink']
    path = 'data/' + list[0]['name'] + '.zip'

    urllib.request.urlretrieve(url,path)
    print(f'USF压缩包已成功下载到 {path}')

def urlfiletype(url):
    parsed_url = urlparse(url)
    filename = parsed_url.path.split('/')[-1]
    
    return Path(filename).suffix

""" 
getusf('data/filelist.json')

data = GetDownList().getSource(2)
print(data['fileListUrl'])
GetDownList().getList(data['fileListUrl'])
print(data)
"""