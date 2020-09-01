import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeb:
    # 测试方法执行前的准备工作
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
    def teardown(self):
        self.driver.quit()
    def test_selenium(self):
        # 使用xpath定位元素，输入keys
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
        # 直接等待
        WebDriverWait(self.driver, 1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@class="nums_text"]')))
        # 打开第一个搜索结果
        self.driver.find_element(By.XPATH,'//*[@id=1]/h3').click()
        # 隐式等待
        self.driver.implicitly_wait(1)
        # 显示等待
        time.sleep(3)




