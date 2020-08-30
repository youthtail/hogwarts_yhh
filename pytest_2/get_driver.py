

from selenium import webdriver


class GetDriver:

    def setup(self, browser):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    # def teardown(self):
    #
    #     self.driver.close()
    #
    #

