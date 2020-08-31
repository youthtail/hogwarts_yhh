from selenium.webdriver.common.by import By
from .base_page import BasePage
from .login_page import Login
from .register_page import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        ''' 
        类加（)表示实例化对象，（）里的参数列表与init构造方法参数列表一致，供构造方法传参
        一旦实例化对象，构造方法就会调用
        '''
        return Login(self._driver)

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)
