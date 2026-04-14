import requests
from requests.exceptions import ConnectionError, ReadTimeout, RequestException

url = "http://www.thelon.cm/xxx.htm"
try:
    req = requests.get(url, timeout=5)
    print(req.status_code)
except ReadTimeout:
    print("Timeout")
except ConnectionError:
    print("Connection error")
except RequestException:
    print("Error")
else:
    if req.status_code == 200:
        print("访问正常！")
        fb = open("t.html", "wb")
        fb.write(req.content)
        fb.close()
    if req.status_code == 404:
        print("页面不存在！")
    if req.status_code == 403:
        print("页面禁止访问！")
