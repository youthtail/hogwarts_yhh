import shelve
from optparse import Option

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSelenium2:
    def setup(self):
        option = Options()
        option._debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        # 吟诗等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_1(self):
        # self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("所有分类").click()
        assert "active" == self.driver.find_element_by_link_text("所有分类").get_property("class")

    def test_get_cookies(self):
        # 把cookies保存到数据库
        # cookies = self.driver.get_cookies()
        # db = shelve.open("mydb/loggincookies")
        # db['cookies'] = cookies
        # db.close()

        # 从数据库读取cookies
        db = shelve.open('mydb/loggincookies')
        cookies:dict = db['cookies']
        db.close()

        # 把cookies加到driver中
        '''
        cookies 是字典的列表
        cookie 是字典，里面有很多k-v
        cookie.pop('exepiry')删除k
        self.driver.add_cookie()，只能加入字典
        '''
        for cookie in cookies:
            if 'exepiry' in cookies.keys():
                cookie.pop('exepiry')
            print(cookie)
            self.driver.add_cookie()

        #   cookies是一个字典列表，需要使用循环加入到driver中


