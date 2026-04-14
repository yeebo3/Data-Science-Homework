import os
import re

import requests

cookie_path = os.path.join(os.path.dirname(__file__), "..", "taobao.txt")
f = open(cookie_path, "r")
cookies = {}
for line in f.read().split(";"):
    name, value = line.strip().split("=", 1)
    cookies[name] = value

r = requests.get("https://www.taobao.com/", cookies=cookies)
rs = re.findall("<title>.*</title>", r.text)
print(rs)
