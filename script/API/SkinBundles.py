import os
from tools import Tools

_BundlesURL = "https://valorant-api.com/v1/bundles"
_BundlesURLJSONPath = "../json/bundles.json"

def downLoadAllBundlesIcon(data):
    for item in data:
        if item['displayName']:
            # 这个系列的名字特殊处理下
            if item['displayName'] == 'Give Back // 2022':
                item['displayName'] = 'Give Back2022'

            dir_path = '../res/bundles/' + item['displayName']


            if not os.path.exists(dir_path):
                os.makedirs(dir_path, True)

        if item['displayIcon']:
            pic_name = "../res/bundles/" + item['displayName'] + '/' + item['uuid'] + ".jpg"
            downLoadPic(item['displayIcon'], pic_name)

        if item['displayIcon2']:
            pic_name = "../res/bundles/" + item['displayName'] + '/' + item['uuid'] + "_displayIcon2" + ".jpg"
            downLoadPic(item['displayIcon2'], pic_name)

def downLoadPic(url, pic_path):
    if not url:
        return

    if not pic_path:
        return

    if os.path.exists(pic_path):
        {}
    else:
        pic = Tools.getContentByUrl(url, Tools._TIMEOUT)
        if pic.content:
            fp = open(pic_path, "wb")
            fp.write(pic.content)
            fp.close()

def start():
    json_data = Tools.getJSONDataByUrl(_BundlesURL)
    Tools.saveJSONData(_BundlesURLJSONPath, json_data, "uuid")

    if json_data:
        downLoadAllBundlesIcon(json_data)