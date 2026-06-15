import json
import re
import os
import requests

class GetDownList:
    def getSource(self,numSource=None):# numSource 下载源编号,如不填写则默认使用一号下载源
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
                if item['number'] == int(downSource):
                    return item
 

    def getList(self,url):
        try:
            response = requests.get(url, timeout=(10,15))
            response.encoding = 'utf-8'
        except:
            print('无法获取文件列表，请检查网络连接以及服务器地址是否正确。')
            return
        
        directory = './data/filelist.js'
        print(os.path.abspath(directory))

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

class GetFile:
    def __init__(self, savedir='../data/'):
        self.savedir = os.path(savedir)

class JsToJson:
    def __init__(self, filepath):
        try:
            with open(filepath, 'r') as file:
                pass
        except:
            print('请检查文件目录是否正确')
            return
    
    




data = GetDownList().getSource(2)
print(data['fileListUrl'])
GetDownList().getList(data['fileListUrl'])
print(data)