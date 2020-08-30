from get_driver import GetDriver


class TestWindow(GetDriver):
    def test_window(self):
        self.driver.get('https://www.baidu.com/')
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text('立即注册').click()
        # 获取窗口
        window = self.driver.window_handles
        # 切换窗口
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys("yanghuihui")
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('11111')
        # 切换窗口
        self.driver.switch_to_window(window[-2])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys("yanghuihui")
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('11111')

