from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()

    #   点击事件
    @pytest.mark.skip
    def test_ActionChains_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # 隐式等待
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'[value="dbl click me"]')))
        element_double_click = self.driver.find_element_by_css_selector('[value="dbl click me"]')
        element_click = self.driver.find_element_by_css_selector('[value="click me"]')
        element_right_click = self.driver.find_element_by_css_selector('[value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        action.context_click(element_right_click)
        action.perform()

    # 移动鼠标
    def test_ActionChains_move(self):
        self.driver.get("https://www.baidu.com/")
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_id("s-usersetting-top")).perform()

    # 拖拽事件
    def test_ActionChains_drag(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        action = ActionChains(self.driver)
        element_source = self.driver.find_element_by_id("dragger")
        for i in range(2,6): # 左闭右开
            element_target = self.driver.find_element_by_xpath(f"/html/body/div[{i}]")
            action.drag_and_drop(element_source,element_target).perform()

    # 键盘控制
    def test_ActionChains_keys(self):
        self.driver.get("http://sahitest.com/demo/keypress.htm")
        action = ActionChains(self.driver)
        action.click(self.driver.find_element_by_xpath('/html/body/form/input[1]'))
        action.send_keys("yang").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("hhi").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
