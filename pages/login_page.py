from pages.base_page import BasePage
from pages.locators import login_loc as loc


class LogInPage(BasePage):
    page_url = '/login'

    @property
    def main_title(self):
        return self.find(loc.title)

    def datas(self, email, passw):
        self.find(loc.email).send_keys(email)
        self.find(loc.passw).send_keys(passw)
        self.find(loc.login_btn).click()

    @property
    def click_forget_passw(self):
        return self.find(loc.forget_passw)

    @property
    def click_login(self):
        return self.find(loc.login_btn)

    @property
    def click_registr(self):
        return self.find(loc.or_registr)

    @property
    def checkbox(self):
        return self.find(loc.checkbox)

