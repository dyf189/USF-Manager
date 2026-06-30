from filehandle import *
from jsonhandle import *
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command', help='子命令')#创建子命令
subparsers.add_parser('get', help='下载最新USF版本')
subparsers.add_parser('update', help='更新USF文件列表')
subparsers.add_parser('list', help='查看USF文件列表及描述')
subparsers.add_parser('install', help='在你的服务器上安装或更新USF')
subparsers.add_parser('view', help='查看USF版本详情')

#可选参数
parser.add_argument('-s', '--source',type=int, help='指定下载源，如果你想添加下载源或查看下载源编号可以查看配置文件')

args = parser.parse_args()


if args.command == 'get':
    getusf('data/filelist.json')
elif args.command == 'update':
    print('正在更新文件列表...')
    data = getSource(args.source) #注：当未指定下载源时，getSource会默认使用json配置里的默认下载源
    #print(data['fileListUrl'])
    getList(data['fileListUrl'])
    #print(data)

    type = urlfiletype(data['fileListUrl'])
    if type == '.js':
        jstojson("data/filelist.js")

    print('文件列表更新完成')
elif args.command == 'list':
    listview()
elif args.command == 'install':
    pass
elif args.command == 'view':
    pass
else:
    print('请检查命令是否填写或正确，输入-h或--help获取帮助')
