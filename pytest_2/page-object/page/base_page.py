from selenium import webdriver


class BasePage:
    _base_url = ''

    def __init__(self, driver: webdriver = None):
        if driver is None:
            self._driver = webdriver.Firefox()
        else:
            self._driver = driver
        if self._base_url != '':
            self._driver.get(self._base_url)

    def find_(self, by, locator):
        return self._driver.find_element(by, locator)

