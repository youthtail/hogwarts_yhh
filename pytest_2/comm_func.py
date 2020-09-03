import os
import shelve

from selenium.webdriver.chrome.webdriver import WebDriver


class CommFunc:
    def save_to_db(self, filename: str, driver: WebDriver):
        path = "mydb" + f"/{filename}"
        db = shelve.open(path)
        db[filename] = driver.get_cookies()
        db.close()

    def get_from_db(self, filename: str) -> str:
        path = "mydb" + f"/{filename}"
        db = shelve.open(path)
        data = db[filename]
        db.close()
        return data



