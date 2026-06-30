import json5
import json
import re

def jstojson(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            listJs = file.read()
    except:
        print('请检查文件目录是否正确')
        return
        
    match = re.search(r'const\s+files\s*=\s*(\[[\s\S]*?\]);', listJs)

    array_str = match.group(1)
    data = json5.loads(array_str)

    with open("data/filelist.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def listview():
    with open('data/filelist.json', 'r', encoding='utf-8') as file:
        list = json.load(file)
        
    print('当前USF版本列表：')
    for i in range(len(list)): #len将python对象返回为列表长度
        if i == 0:
           print("· " + list[i]['name'] + "(最新版本)" + " " + list[i]['description'])#最新版本
           i=+1
        else:
            print("· " + list[i]['name'] + " " + list[i]['description'])
            i=+1

#jstojson("data/filelist.js")  