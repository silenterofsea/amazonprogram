from settings import PROXY_POOL_URL
from btEmail import bt_api
import requests
from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import time




class AmazonClass(object):
    def __init__(self):
        self.password = 'aaaBBBccc123!@#'
        self.target_ulr = 'https://www.amazon.com/'
        self.browser = browser = webdriver.Chrome('/snap/bin/chromium.chromedriver')

    def __del__(self):
        self.browser.close()

    def get_email(self):
        '''
        在邮箱系统中生成一个邮箱
        :return: 成功返回，邮箱地址
                 失败返回， None
        '''
        bt_mail = bt_api()
        bt_mail.set_mail()

    def get_addr(self):
        # 获取注册地址
        pass

    def get_card(self):
        # 获取信用卡号
        pass

    def get_proxy(self):
        # 获取代理IP
        try:
            res = requests.get(PROXY_POOL_URL)
            if res.status_code == 200:
                return res.text
        except Exception:
            return None



    def run(self):
        self.browser.get("https://www.amazon.com")
        time.sleep(3)
        print(self.browser.current_url)
        print(self.browser.get_cookies())
        self.browser.find_element_by_link_text("Start here.").click()
        self.get_email()

if __name__ == '__main__':
    ac = AmazonClass()
    ac.run()
