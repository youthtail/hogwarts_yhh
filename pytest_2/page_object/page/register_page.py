from selenium.webdriver.common.by import By

from page_object.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.CSS_SELECTOR, "#corp_name").send_keys("hello")
        return True
