from getfile import *
from filejson import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source',type=int, help='指定下载源，如果你想添加下载源或查看下载源编号可以查看配置文件')

args = parser.parse_args()

data = getSource(args.source)
print(data['fileListUrl'])
getList(data['fileListUrl'])
print(data)
jstojson("data/filelist.js")

