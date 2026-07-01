import zipfile
import os
import shutil

def unzip(path, extract_to):
    if not os.path.exists(extract_to + '/usf'):
        os.makedirs(extract_to + '/usf')
    else:
        shutil.rmtree(extract_to + '/usf')
        os.makedirs(extract_to + '/usf')
        
    with zipfile.ZipFile(path, 'r') as zip:
        zip.extractall(extract_to + '/usf')

def unmcpack(path, extract_to):
    if not os.path.exists(extract_to + '/usf/usf'):
        os.makedirs(extract_to + '/usf/usf')
    else:
        shutil.rmtree(extract_to + '/usf/usf')
        os.makedirs(extract_to + '/usf/usf')
        
    with zipfile.ZipFile(path, 'r') as zip:
        zip.extractall(extract_to + '/usf/usf')

def findusf(path):
    for i in os.listdir(path):
        if i.endswith('.mcpack'):
            return i
