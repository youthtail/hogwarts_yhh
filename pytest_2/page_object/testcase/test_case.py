from page_object.page.base_page import BasePage
from page_object.page.main_page import Main


class TestCase:
    # 实例化Main对象并赋值给main,每个方法执行前调用
    def setup(self):
        self.main = Main()
    def teardown(self):
        self.main._driver.close()

    def test_register(self):
        assert self.main.goto_register().register()
    def test_login(self):
        assert self.main.goto_login().scan()
    def test_login_to_registe(self):
        assert self.main.goto_login().to_register().register()

