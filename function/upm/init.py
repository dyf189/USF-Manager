from getfile import *
from filejson import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo', type=str, help='给UPM传入参数')
parser.add_argument('-s', '--source',type=int, help='指定下载源，如果你想添加下载源或查看下载源编号可以查看配置文件')

args = parser.parse_args()


if args.echo == 'get':
    getusf('data/filelist.json')
elif args.echo == 'update':
    print('正在更新文件列表...')
    data = getSource(args.source)
    #print(data['fileListUrl'])
    getList(data['fileListUrl'])
    #print(data)
    jstojson("data/filelist.js")
    print('文件列表更新完成')
