import urllib.robotparser

import requests


robot = urllib.robotparser.RobotFileParser()
robot.set_url("https://item.taobao.com/robots.txt")
robot.read()

useragent = "Baiduspider"
url = "https://item.taobao.com/item.htm?spm=a310p.7395781.1998038982.1&id=16041384170"

if robot.can_fetch(useragent, url):
    print("允许抓取")
    response = requests.get(url, timeout=10)
    with open("bd-html.html", "wb") as file:
        file.write(response.content)
else:
    print("不允许抓取")
