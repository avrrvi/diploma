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

    def click_day(self):
        return self.find(loc.choose_day).click()

    def input_data(self, name, prot, fats, carboh, cal, weight):
        self.find(loc.text_name).send_keys(name)
        self.find(loc.text_proteins).send_keys(prot)
        self.find(loc.text_fats).send_keys(fats)
        self.find(loc.text_carbohydrates).send_keys(carboh)
        self.find(loc.text_cal).send_keys(cal)
        self.find(loc.text_weight).send_keys(weight)

    def click_add_btn(self):
        return self.find(loc.add_btn).click()

    def result_table(self):
        self.wait_until_visibility(loc.wait)
        return self.find(loc.res_table)

    def del_field(self):
        return self.find(loc.wait).click()

    def total(self):
        return self.find(loc.total).text

