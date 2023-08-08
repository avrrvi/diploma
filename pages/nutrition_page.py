from pages.base_page import BasePage
from pages.locators import nutrition_loc as loc
from pages.locators import login_loc


class NutritionPage(BasePage):
    page_url = '/login'

    def registr(self, email, passw):
        self.find(login_loc.email).send_keys(email)
        self.find(login_loc.passw).send_keys(passw)
        self.find(login_loc.login_btn).click()


    def click_page(self):
        return self.find(loc.page).click()
