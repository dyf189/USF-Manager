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

#jstojson("data/filelist.js")  