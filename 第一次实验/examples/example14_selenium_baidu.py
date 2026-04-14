import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r"geckodriver.exe")
browser.get("https://www.baidu.com/")
time.sleep(2)
input = browser.find_element_by_name("wd")
input.send_keys("信息检索")
input.send_keys(Keys.ENTER)
print(browser.current_url)
print(browser.page_source)
time.sleep(2)
