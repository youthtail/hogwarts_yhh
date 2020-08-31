from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 成员变量
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        self._driver = ''
        if driver is None:
            # 成员变量，动态添加
            self._driver = webdriver.Firefox()
        else:
            self._driver = driver
        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

