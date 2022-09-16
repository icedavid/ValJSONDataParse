# @desc: 纯纯工具类,需要添加的工具类组件全部放这里统一调用
import requests

_TIMEOUT = 10

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