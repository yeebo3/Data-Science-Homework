# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><body><div id="second-title">访华前 这个国家的总理说“感谢中国体谅”</div>
<div class="date-source">
<span class="date">2019年03月27日 21:30</span></div>
<span class="publish source">参考消息</span>
<div class="article">
<p>原标题：锐参考 | 访华前，这个国家的总理说：“感谢中国体谅！”</p>
<p>“非常感谢中国的理解！”</p>
<p>在25日的新闻发布会上，新西兰总理杰辛达·阿德恩这样说道。</p>
</div>
</body></html>
"""
soup = BeautifulSoup(html, "lxml")
title = soup.select("div#second-title")[0].text
date = soup.select("span.date")[0].text
source = soup.select("span.publish.source")[0].text
content = soup.select("div.article > p")
contentstr = ""
for i in range(len(content)):
    contentstr += content[i].text + "\n"

print("标题：", title)
print("发布日期：", date)
print("消息来源：", source)
print("消息内容：", contentstr)
