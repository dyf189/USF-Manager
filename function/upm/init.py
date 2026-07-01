from filehandle import *
from jsonhandle import *
from installusf import *
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command', help='子命令')#创建子命令

parserGet = subparsers.add_parser('get', help='下载最新USF版本')
parserUpdate = subparsers.add_parser('update', help='更新USF文件列表')
subparsers.add_parser('list', help='查看USF文件列表及描述')
parserInstall = subparsers.add_parser('install', help='在你的服务器上安装或更新USF')
subparsers.add_parser('view', help='查看USF版本详情')

#可选参数
parserUpdate.add_argument('-s', '--source',type=int, help='指定用于更新列表的下载源，如果你想添加下载源或查看下载源编号可以查看配置文件')
parserGet.add_argument('-i', '--install', type=bool, default=False, help='在使用get命令时同时对USF进行安装或更新')
parserInstall.add_argument('-p', '--path', default='data', help='指定USF压缩包的解压路径')

args = parser.parse_args()


if args.command == 'get':
    getusf('data/filelist.json')

    if args.install == True:
        pass
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
    zippath = getusf('data/filelist.json', get=False)
    unzip(zippath, args.path)
    unmcpack(('data/usf/' + findusf('data/usf')), args.path)
elif args.command == 'view':
    pass
else:
    print('请检查命令是否填写或正确')
    parser.print_help()
