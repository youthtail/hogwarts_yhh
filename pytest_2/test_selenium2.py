import shelve
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSelenium2:
    def setup(self):
        option = Options()
        option._debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        # self.driver.get("https://ceshiren.com/")
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
        # # 把cookies保存到数据库
        # cookies = self.driver.get_cookies()
        # # mydb目录要提前创建
        # db =shelve.open('mydb/logincookies')
        # db['cookies'] = cookies
        # db.close()

        # 从数据库读取cookies
        db = shelve.open('mydb/logincookies')
        cookies = db['cookies']
        db.close()

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
                print(cookie)
                cookie.pop('expiry')
                print(cookie)
            self.driver.add_cookie(cookie)


