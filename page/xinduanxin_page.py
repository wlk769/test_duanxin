import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction





class XinDuanXinPage(BaseAction):
    jieshou_text = By.ID,"com.android.mms:id/recipients_editor"
    neirong_text = By.ID,"com.android.mms:id/embedded_text_editor"
    send_btn = By.XPATH,"//*[@content-desc = '发送']"
    @allure.step(title = '输入文字')
    def input_jieshou_text(self,text):
        allure.attach('输入', text, allure.attach_type.TEXT)
        self.input(self.jieshou_text,text)
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    def input_neirong_text(self,text):
        self.input(self.neirong_text,text)

    def click_send_btn(self):
        self.click(self.send_btn)
