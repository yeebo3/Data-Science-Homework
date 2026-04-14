import requests
from requests.exceptions import ConnectionError, ReadTimeout, RequestException


urls = [
    "http://www.kd008.com/server.php?sid=1",
    "http://www.hzau.edu.cn",
]

for url in urls:
    print(url)
    try:
        response = requests.get(url, timeout=5)
        print(response.status_code)
    except ReadTimeout:
        print("Timeout")
    except ConnectionError:
        print("Connection error")
    except RequestException:
        print("Error")
    else:
        if response.status_code == 200:
            print("访问正常！")
        elif response.status_code == 404:
            print("页面不存在！")
        elif response.status_code == 403:
            print("页面禁止访问！")
