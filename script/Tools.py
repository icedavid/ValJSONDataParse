# @desc: 纯纯工具类,需要添加的工具类组件全部放这里统一调用
from base64 import encode
import json
import requests
import os

_TIMEOUT = 10

_DefalutSavePath = "../res/local"
 
# @brief: 初始化资源路径
def initResDir(res_path):
    if res_path and not os.path.exists(res_path):
        os.makedirs(res_path, True)

def getContentByUrl(url, timeout):
    target = requests.get(url, timeout = timeout)
    if target:
        return target
    else:
        return None

def getJSONDataByUrl(url):
    if not url:
        return None
    else:
        f = getContentByUrl(url, _TIMEOUT)
        if f:
            jsonData = f.json()
            if jsonData and jsonData['status'] == 200:
                return jsonData['data']
            else:
                return None
        else:
            assert("解析Url地址失败，请稍后重试！")

# @brief: 保存JSON数据，根据参数决定用什么关键字作为key存储
def saveJSONData(save_path, data_list, key_name):
    save_path = save_path or _DefalutSavePath

    if not data_list:
        print("Tools.saveJSONData data_list is empty list!!!")
        return None

    temp_list = {}
    if key_name and type(key_name) == 'str':
        for item_data in data_list:
            if item_data[key_name]:
                key = item_data[key_name]
                temp_list[key] = item_data
    
    encode_data  = temp_list or data_list
    f = open(save_path, 'w')
    f.write(encode_data)
    f.close()

def createDirByKey(data, dir_path, key_name):
    if not dir_path:
        print("createDirByThemeUuid dir_path is empty!!!")
        return None

    if not key_name:
        print("createDirByThemeUuid key_name is empty!!!")
        return None

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if data:
        for item in data:
            if item[key_name]:
                path = dir_path + item[key_name]
                if not os.path.exists(path):
                    os.makedirs(path, True)