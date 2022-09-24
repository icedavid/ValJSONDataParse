import Tools

_ThemeURL = "https://valorant-api.com/v1/themes"
_ThemeURLJSONPath = "../json/theme.json"

def init():
    print("init")

# @brief: 将SkinImage中的getJSONDataByUrl抽象过来做通用类
def start():
    json_data = Tools.getJSONDataByUrl(_ThemeURL)
    Tools.saveJSONData(_ThemeURLJSONPath, json_data, 'uuid')
    if json_data:
        print("json_data is not empty!!!")