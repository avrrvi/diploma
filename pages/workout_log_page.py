from pages.base_page import BasePage
from pages.locators import workout_log_loc as loc
from pages.locators import login_loc


class WorkOutPage(BasePage):
    page_url = '/login'

    def registr(self, email, passw):
        self.find(login_loc.email).send_keys(email)
        self.find(login_loc.passw).send_keys(passw)
        self.find(login_loc.login_btn).click()

    @property
    def add_workout_btn(self):
        return self.find(loc.add_workout)

    def wait(self):
        return self.wait_until_visibility(loc.add_workout_2)

    @property
    def add_workout_btn_2(self):
        return self.find(loc.add_workout_2)


