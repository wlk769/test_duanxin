from page.duanxin_page import DuanXinPage
from page.xinduanxin_page import XinDuanXinPage


class Page:
    def __init__(self,driver):
        self.driver = driver
    @property
    def duanxinpage(self):
        return DuanXinPage(self.driver)
    @property
    def xinduanxinage(self):
        return  XinDuanXinPage(self.driver)

