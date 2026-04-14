import urllib.robotparser

import requests

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://item.taobao.com/robots.txt")
rp.read()

useragent = "Googlebot"
url = "https://item.taobao.com/item.htm?spm=a310p.7395781.1998038982.1&id=16041384170"
if rp.can_fetch(useragent, url):
    print("允许抓取")
    file = requests.get(url)
    data = file.content
    fb = open("bd-html", "wb")
    fb.write(data)
    fb.close()
else:
    print("不允许抓取")
