from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DuanXinPage(BaseAction):

    duanxin_btn = By.ID,"com.android.mms:id/action_compose_new"

    def click_duanxin_btn(self):
        self.click(self.duanxin_btn)





