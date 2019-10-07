import time
import pytest

from base.base_driver import init_driver
from page.page import Page


class TestDuanXin:
    def setup(self):
        self.driver =init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(("phone","contect"),[("18888888888","hello"),("13333333333","abc")])
    def test_duanxin(self,phone,contect):
        self.page.duanxinpage.click_duanxin_btn()
        self.page.xinduanxinage.input_jieshou_text(phone)
        self.page.xinduanxinage.input_neirong_text(contect)

        self.page.xinduanxinage.click_send_btn()


