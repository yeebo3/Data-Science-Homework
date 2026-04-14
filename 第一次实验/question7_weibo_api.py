import json
from urllib import parse

import requests


def get_weibo_ids(access_token, uid, header_dict):
    url = "https://api.weibo.com/2/statuses/user_timeline/ids.json"
    url_dict = {"access_token": access_token, "uid": uid}
    url_param = parse.urlencode(url_dict)
    response = requests.get(url="%s?%s" % (url, url_param), headers=header_dict)
    decode_data = json.loads(response.text)
    return decode_data["statuses"]


def get_weibo_text(access_token, wid, header_dict):
    url = "https://api.weibo.com/2/statuses/show.json"
    url_dict = {"access_token": access_token, "id": wid}
    url_param = parse.urlencode(url_dict)
    response = requests.get(url="%s?%s" % (url, url_param), headers=header_dict)
    decode_data = json.loads(response.text)
    text = decode_data["text"]
    if "retweeted_status" in decode_data:
        text += "     <---原始微博：" + decode_data["retweeted_status"]["text"]
    return text


header_dict = {"User-Agent": "Mozilla/5.0"}
access_token = "请填写自己的access_token"
uid = "请填写喜欢的明星uid"

if access_token != "请填写自己的access_token" and uid != "请填写喜欢的明星uid":
    wid_list = get_weibo_ids(access_token, uid, header_dict)
    for item in wid_list:
        weibo_text = get_weibo_text(access_token, item, header_dict)
        print("微博id:" + str(item) + "--->" + weibo_text + "\n")
