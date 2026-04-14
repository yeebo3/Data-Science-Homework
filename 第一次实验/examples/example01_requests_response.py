import requests

r = requests.get(
    "http://www.hzau.edu.cn/",
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10,
)
r.encoding = "utf-8"
print(r.text)
