# @desc: 纯纯工具类,需要添加的工具类组件全部放这里统一调用
import requests

def getContentByUrl(url, timeout):
    target = requests.get(url, timeout = timeout)
    if target:
        return target
    else:
        return None