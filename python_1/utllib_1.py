import urllib.request
rsp: object = urllib.request.urlopen('www.baidu.com')
print(rsp.status)

