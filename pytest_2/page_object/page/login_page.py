from selenium.webdriver.common.by import By
from page_object.page.base_page import BasePage
from page_object.page.register_page import Register


class Login(BasePage):
    def scan(self):
        return True

    def to_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)
