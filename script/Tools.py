# @desc: 纯纯工具类,需要添加的工具类组件全部放这里统一调用
from operator import truediv
import time
import json
import requests
import os

from base64 import encode
from tqdm import tqdm

_TIMEOUT = 10
_GRANTIME = 100

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

# @brief: 根据key_name创建对应的文件夹
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
        for i in tqdm(range(_GRANTIME)):
            for item in data:
                if item[key_name]:
                    path = dir_path + item[key_name]
                    if not os.path.exists(path):
                        os.makedirs(path, True)

# @breif: 下载的数据保存到指定的目录下,文件是否创建成功返回bool值
def saveFile(path, data):
    # 目录没有就创建
    if path:
        if not os.path.exists(path):
            os.makedirs(path, True)

    if data:
        fp = open()
        fp.write(data)
        fp.close()
        return True
    else:
        return False

# @beidf: 计算程序的执行时间,callback 是要检测的函数,desc是添加的打印
def calculateTime(callback, desc):
    if callback:
        desc = desc or "Tools.calculateTime "
        start_time = time.time()
        callback()
        over_time = time.time()
        print("{}总耗时：{}".format(desc, over_time - start_time))
    else:
        print("Not callback function is not allow!!!")