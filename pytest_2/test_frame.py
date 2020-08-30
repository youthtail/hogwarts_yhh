from get_driver import GetDriver


class TestFrame(GetDriver):

    def setup(self):
        super().setup("firefox")

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=tryhtml_frame_noresize")
        # self.driver.switch_to_frame(self.dr/ver.find_element_by_xpath('//*/frame[1]'))

        self.driver.switch_to_frame(2)

        """
         Usage:
            driver.switch_to.frame('frame_name') :id 的值
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])，
        
        """
        print(self.driver.find_element_by_css_selector('frame[src="frame_b.htm"]').text)
