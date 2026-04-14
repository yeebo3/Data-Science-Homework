import requests

url = "http://www.hzau.edu.cn/"
useragent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"
http_headers = {
    "User-Agent": useragent,
    "Accept": "text/html",
}
page = requests.get(url, headers=http_headers)
print(page.status_code)
