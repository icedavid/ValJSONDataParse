import time
import json
import os

from tqdm import tqdm
from tools import Tools

from logging import exception
from pprint import pprint

_SkinURL = "https://valorant-api.com/v1/weapons/skins"
_SkinURLJSONPath = "..\\json\\skin.json"
_TIMEOUT = 10
_RES_PATH = '../res/'

''' 
    @brief: 主函数处理流程
        + √ @API getJSONDataByUrl
                通过http请求获取到val API上的皮肤数据 
        + √ @API saveJSONDataByUuid
            解析json数据保存到本地上，建立字典（key为uuid）去存储皮肤信息
        + @API downLoadAllIcon遍历数据的icon地址去下载到本地保存
            + 用themeUuid去建立文件夹保存对应系列的皮肤，暂定接口为createDirByThemeUuid

        @Tips: 目前使用到的工具类都放入到Tools中，这样其他脚本写的时候就直接对应相关api就好，避免重复造轮子
'''

# @brief: 将转换的key为uuid的skin.json保存到本地中
def saveJSONDataByUuid(dic):
    listByUuid = {}
    for itemData in dic:
        if itemData['uuid']:
            key = itemData['uuid']
            listByUuid[key] = itemData

    encodeData = json.dumps(listByUuid)
    f = open(_SkinURLJSONPath, 'w')
    f.write(encodeData)
    f.close()

# @brief: 根据ThemeUuid来创建文件夹
def createDirByThemeUuid(dic):
    skinDoc = os.path.exists(_RES_PATH + 'skin')
    if not skinDoc:
        os.makedirs(_RES_PATH + 'skin')

    if dic:
        for t in tqdm(range(100)):
            for item in dic:
                if item['displayIcon']:
                    if item['themeUuid']:
                        path = '../res/skin/' + item['themeUuid']
                        folder = os.path.exists(path)
                        # 存在文件夹就跳过，没有就创建
                        if not folder:
                            os.makedirs(path, True)
                            # print("%s 文件夹创建成功！", item['themeUuid'])

                    # 下载文件，保存到本地中,先检查文件是否存在
                    picName = "../res/skin/" + item['themeUuid'] + '/' + item['uuid'] + '.jpg'
                    picFile = os.path.exists(picName)
                    if picFile:
                        # print("{}文件已存在！".format(item['uuid']))
                        {}
                    else:
                        pic = Tools.getContentByUrl(item['displayIcon'], _TIMEOUT)
                        if pic.content:
                            fp = open(picName, 'wb')
                            fp.write(pic.content)
                            fp.close()

# @brief: 根据displayIcon去下载对应的图片
# 用关键字themeUuid去创建对应的文件夹，存入对应的目录下
def downLoadAllIcon(dic):
    if dic:
        for item in dic:
            if item['displayIcon']:
                pic = Tools.getContentByUrl(item['displayIcon'], _TIMEOUT)
                picName = "../res/skin/" + item['themeUuid'] + '/' + item['uuid'] + '.jpg'
                if pic.content:
                    fp = open(picName, 'wb')
                    fp.write(pic.content)
                    fp.close()

def start():
    jsonData = Tools.getJSONDataByUrl(_SkinURL)
    Tools.saveJSONData(_SkinURLJSONPath, jsonData, 'uuid')

    if jsonData:
        createDirByThemeUuid(jsonData)