import requests

# http_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# r=requests.get("https://www.hzau.edu.cn/",headers=http_headers,timeout=10)
# print(r.status_code)
# # print(r.text)
# r.encoding='utf-8'
# print(r.encoding)
# #思考题1
# import dns.resolver
# dns_cache=[]  #纯列表，每个元素是[域名，IP]
# def get_ip(domain):
#     for item in dns_cache:
#         if item[0]==domain:
#             return item[1]
        
#     a=dns.resolver.query(domain,"A")

#     ip=a.response.answer[0].to_text().split(" ")[-1]
#     dns_cache.append([domain,ip])
#     return ip

# #测试思考1函数
# print(get_ip("www.hzau.edu.cn"))

# #思考题2
# import urllib.robotparser as ur

# rp=ur.RobotFileParser()
# rp.set_url("https://item.taobao.com/robots.txt")
# rp.read()
# print(rp)

# useragent='Bdiduspider'

# url='https://item.taobao.com/item.htm?spm=a310p.7395781.1998038982.1&id=16041384170'
# if rp.can_fetch(useragent,url):
#     print("可以访问")
#     file=requests.get(url)
#     data=file.content
#     fb=open("bd-html.html","wb")
#     fb.write(data)
#     fb.close()
# else:
#     print("不能访问")

# from requests.exceptions import ReadTimeout,ConnectionError,RequestException

# url = ['http://www.thelon.cm/xxx.htm','http://www.kd008.com/server.php?sid=1','www.hzau.edu.cn']
# for i in range(3):
#     print(url[i])
#     try:
#         req=requests.get(url[i],timeout=5)
#         print(req.status_code)
#     except ReadTimeout:
#         print("读取超时")
#     except ConnectionError:
#         print("连接错误")
#     except RequestException:
#         print("请求异常")
#     else:
#         if req.status_code==200:
#             fb=open(url[i].split("/")[-1]+".html","wb")
#             fb.write(req.content)
#             fb.close()
#         elif req.status_code==404:
#             print("页面不存在")
#         elif req.status_code==403:
#             print("页面拒绝访问")

import re
s='''<li><a href="http://news.sina.com.cn/o/2018-11-06/a75.shtml" target="_blank">进博会</a></li>
<li><a href="http://news.sina.com.cn/o/2018-11-06/a76.shtml" target="_blank">大数据</a></li>
<li><a href="/o/2018-11-06/a75.shtml" target="_blank">进博会</a></li>'''
urls=re.findall('<a href="http://[a-zA-Z0-9/\.\-:]+"', s)

url_test=re.findall('<a href="[^"]+"', s)
print(url_test)
for url in url_test:
   print(url[9:len(url)-1])

