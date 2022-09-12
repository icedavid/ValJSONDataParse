
import requests
import json

from logging import exception
from pprint import pprint

_SkinURL = "https://valorant-api.com/v1/weapons/skins"
_SkinURLJSONPath = "..\\json\\skin.json"
SkinDic = None

''' 
    @brief: 主函数处理流程
        + √ @API getJSONDataByUrl
                通过http请求获取到val API上的皮肤数据 
        + √ @API saveJSONDataByUuid
            解析json数据保存到本地上，建立字典（key为uuid）去存储皮肤信息
        + @API downLoadAllIcon遍历数据的icon地址去下载到本地保存
            + 用themeUuid去建立文件夹保存对应系列的皮肤
'''
def main():
    jsonData = getJSONDataByUrl(_SkinURL)
    saveJSONDataByUuid(jsonData)
    downLoadAllIcon(jsonData)

# @brief: 通过API获取JSON数据
def getJSONDataByUrl(url):
    if not url:
        print("@getJSONDataByUrl url is null!!!!")
        return None

    f = requests.get(url)

    # 这里直接解析为python对象
    jsonData = f.json()
    if jsonData:
        if jsonData['status'] == 200:
            return jsonData['data']
        else:
            print("状态码为：" + jsonData['status'] +  "，获取数据失败")
            return None

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

# @brief: 根据displayIcon去下载对应的图片
# 用关键字themeUuid去创建对应的文件夹，存入对应的目录下
def downLoadAllIcon(dic):
    if dic:
        for item in dic:
            if item['displayIcon']:
                pic = requests.get(item['displayIcon'], timeout = 5)
                picName = "../res/skinIcon/" + item['uuid'] + '.jpg'
                fp = open(picName, 'wb')
                fp.write(pic.content)
                fp.close()

