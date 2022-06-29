# -*- coding = utf-8 -*-'
# Author    : 张家俊
# @Time     : 2022/6/21 21:32
# @File     : 自动体温打卡.py
# @software : PyCharm
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def tiwendaka():
    url = "http://xscfw.hebust.edu.cn/survey/login"
    user = ""     # 账号
    password = ""     # 密码

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)

    # 登陆
    browser.get(url)
    browser.find_element("xpath", "/html/body/div[1]/div[2]/form/div[1]/input").send_keys(user)
    browser.find_element("xpath", "/html/body/div[1]/div[2]/form/div[2]/input").send_keys(password)
    browser.find_element("xpath", "/html/body/div[1]/div[2]/div/div/button").click()
    time.sleep(1)

    ActionChains(browser).move_to_element(browser.find_element("xpath", "/html/body/ul/li[1]/div")).click().perform()
    time.sleep(3)

    browser.find_element("xpath", "/html/body/form/div[2]/div[2]/input").send_keys("36.5")  # 填上午体温36.5
    browser.find_element("xpath", "/html/body/form/div[2]/div[5]/input").send_keys("36.5")  # 填下午体温36.5
    browser.find_element("xpath", "/html/body/form/div[2]/div[7]/label[2]").click()     # 点击健康
    time.sleep(3)

    browser.find_element("xpath", "/html/body/button").click()  # 提交
    time.sleep(3)

    browser.close()

tiwendaka()