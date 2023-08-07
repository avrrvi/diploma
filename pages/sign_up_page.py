from pages.base_page import BasePage
from pages.locators import sign_up_loc as loc


class SignUpPage(BasePage):
    page_url = '/registration/'

    @property
    def main_title(self):
        return self.find(loc.title)

    @property
    def signup_by_vk(self):
        return self.find(loc.signup_by_vk)

    @property
    def signup_by_apple(self):
        return self.find(loc.signup_by_fb)

    @property
    def signup_by_yandex(self):
        return self.find(loc.signup_by_google)

    @property
    def signup_by_google(self):
        return self.find(loc.signup_by_odnoklassniki)

    def vk_link(self):
        self.find(loc.signup_by_vk).click()

    def apple_link(self):
        self.find(loc.signup_by_fb).click()

    def yandex_link(self):
        self.find(loc.signup_by_google).click()

    def google_link(self):
        self.find(loc.signup_by_odnoklassniki).click()

    # @property
    def conditions(self):
        return self.find(loc.doc)

    def email(self, email):
        return self.find(loc.email).send_keys(email)

    def fname(self, fname):
        return self.find(loc.fname).send_keys(fname)

    def lname(self, lname):
        return self.find(loc.lname).send_keys(lname)

    def passw(self, passw):
        return self.find(loc.password).send_keys(passw)

    def repeat_passw(self, confirm_passw):
        return self.find(loc.confirm_password).send_keys(confirm_passw)

    def sign_up(self):
        self.find(loc.sign_up).click()

    def wait(self):
        return self.wait_until_visibility(loc.wait_loc)

    # @property
    def err_mess(self):
        return self.find(loc.empty_err_mess).text
