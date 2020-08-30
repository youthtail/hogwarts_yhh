import pytest

from get_driver import GetDriver


class TestJS(GetDriver):
    def setup(self):
        super().setup("firefox")

    @pytest.mark.skip
    def test_js_exec1(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_class_name('n').click()
        # js命令分开写法
        # for code in ["return document.title", "return JSON.stringify(performance.timing)"]:
        #     print(self.driver.execute_script(code))
        # js命令合并写法，只能有一个return
        print(self.driver.execute_script("document.title;return JSON.stringify(performance.timing)"))

    '''
    操作时间控件
    1 定位元素
    2 删除readonly属性
    3 赋值
    '''

    def test_js_date(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute('
                                   '"readonly")')
        tt = self.driver.execute_script('document.getElementById("train_date").value="2020-02-02"')
       