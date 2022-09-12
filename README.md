# Val皮肤获取脚本
## 运行逻辑
+ getJSONDataByUrl 通过http请求获取到val API上的皮肤数据 
+ saveJSONDataByUuid 解析json数据保存到本地上，建立字典（key为uuid）去存储皮肤信息、
+ downLoadAllIcon 遍历数据的icon地址去下载到本地保存

## 目前需要实现的逻辑
+ 根据themeUuid去创建对应的文件夹，保存同一系列下的皮肤，分类保存
  + 用themeUuid去找到系列对应的系列名字，用来做文件名
+ 皮肤的模糊查找
+ 待定

