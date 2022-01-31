import json

def readJson(file):
    with open(file, 'r',  encoding='UTF-8') as _file:
        data = _file.read()

    objData = json.loads(data)
    return objData