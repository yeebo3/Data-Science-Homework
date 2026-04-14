import os
import re
import urllib.robotparser

import jieba
import requests
from bs4 import BeautifulSoup
from gensim.corpora.dictionary import Dictionary


def savefile(file_dir, content, seq):
    file_path = file_dir + os.sep + str(seq) + ".html"
    f = open(file_path, "wb")
    f.write(content.encode("utf-8"))
    f.close()


useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
http_headers = {
    "User-Agent": useragent,
    "Accept": "text/html",
}

topicwords = {"网络", "安全", "法案", "预警", "设施", "互联网"}

website = "http://roll.news.sina.com.cn/"
url = "http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml"
file_dir = "."

rp = urllib.robotparser.RobotFileParser()
rp.set_url(website + "robots.txt")
rp.read()

if rp.can_fetch(useragent, url):
    page = requests.get(url, headers=http_headers)
    page.encoding = "gb2312"
    content = page.text

    stop_path = os.path.join(os.path.dirname(__file__), "..", "stopword.txt")
    stoplist = open(stop_path, "r", encoding="utf-8").readlines()
    stoplist = set(w.strip() for w in stoplist)

    ulist = re.findall('href="http://[a-z0-9/.\\-]+\\.shtml', content)
    i = 1
    for u in ulist:
        u = u[6:]
        print(u)
        page = requests.get(u, headers=http_headers)
        page.encoding = "utf-8"
        content = page.text

        bs = BeautifulSoup(content, "lxml")
        ps = bs.select("div#article > p")
        doc = []
        for p in ps:
            p = p.text.strip("\n")
            if p != "":
                d = []
                for w in list(jieba.cut(p, cut_all=True)):
                    if len(w) > 1 and w not in stoplist:
                        d.append(w)
                doc.append(d)

        dictionary = Dictionary(doc)
        dictionary.filter_extremes(no_below=2, no_above=1.0, keep_n=10)
        d = dict(dictionary.items())
        docwords = set(d.values())

        commwords = topicwords.intersection(docwords)
        sim = len(commwords) / (len(topicwords) + len(docwords) - len(commwords))

        if sim > 0.1:
            print(docwords)
            print("sim=", sim)
            savefile(file_dir, content, i)
        i = i + 1
else:
    print("不允许抓取！")
