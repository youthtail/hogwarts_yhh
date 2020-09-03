import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from comm_func import CommFunc


class TestSelenium2:
    def setup(self):
        option = Options()
        option._debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)

        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_1(self):
        self.driver.find_element_by_link_text("所有分类").click()
        assert "active" == self.driver.find_element_by_link_text("所有分类").get_attribute("class")

    @pytest.mark.run(order=1)
    def test_get_cookies(self):
        # mydb目录要提前创建
        # 把cookies保存到数据库
        CommFunc().save_to_db("weixin_token", self.driver)
        cookies = CommFunc().get_from_db("weixin_token")
        print(cookies)


        # 把cookies加到driver中
        '''
        cookies 是字典的列表
        cookie 是字典，里面有很多k-v
        cookie.pop('exepiry')删除k
        self.driver.add_cookie()，只能加入字典
        '''
        #   cookies是一个字典列表，需要使用循环加入到driver中
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.find_element_by_id("menu_contacts").click()
        self.driver.find_element_by_link_text("导入通讯录").click()
        self.driver.find_element_by_id("js_upload_file_input").send_keys("/Users/huihuiyang/Downloads/1.xls")
        assert "1.xls" == self.driver.find_element_by_id("upload_file_name").text


