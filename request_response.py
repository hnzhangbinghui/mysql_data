# 参考URL：https://www.cnblogs.com/xinz-study/p/9294452.html
# coding=utf-8
import requests
import json

# response = requests.get("https://www.baidu.com/")
# response.encoding='utf-8'
#
# # print(type(response))
# # print(response.status_code)
# # print(response.cookies)
# print(response.text)
# # print(response.content)
# # print(response.headers)
# # print(response.content.decode("utf-8"))
# print(response.url)

#Get and post
print("Get*****************************")
data={"userName":"15239687008","Password":"123"}
resp=requests.get("http://jgdj.hnsft.gov.cn:8088/sft/login/get",params=data)
print(resp.url)
# print(resp.text)
print(resp.content)
print(resp.cookies)
# 上述两种的结果是相同的，通过params参数传递一个字典内容，从而直接构造url
# 注意：第二种方式通过字典的方式的时候，如果字典中的参数为None则不会添加到url上
print("Post*****************************")
resp1=requests.post("http://jgdj.hnsft.gov.cn:8088/sft/login/post",data=data)
print(resp1.status_code)
print(resp1.url)
print(resp1.headers)
