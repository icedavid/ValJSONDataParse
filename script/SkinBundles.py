import os
import Tools

_BundlesURL = "https://valorant-api.com/v1/bundles"
_BundlesURLJSONPath = "../json/bundles.json"

def downLoadAllBundlesIcon(data):
    for item in data:
        if item['displayIcon'] or item['displayIcon2']:
            if item['displayName']:
                dir_path = '../res/bundles/' + item['displayName']
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path, True)
            
            pic_name = "../res/bundles/" + item['displayName'] + '/' + item['uuid'] + ".jpg"
            if os.path.exists(pic_name):
                {}
            else:
                pic = Tools.getContentByUrl(item['displayIcon'] or item['displayIcon'], Tools._TIMEOUT)
                if pic.content:
                    fp = open(pic_name, 'wb')
                    fp.write(pic.content)
                    fp.close()

def start():
    json_data = Tools.getJSONDataByUrl(_BundlesURL)
    Tools.saveJSONData(_BundlesURLJSONPath, json_data, "uuid")

    if json_data:
        downLoadAllBundlesIcon(json_data)