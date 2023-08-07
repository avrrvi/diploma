from pages.base_page import BasePage
from pages.locators import template_loc as loc
from pages.locators import login_loc
from pages.locators import workout_log_loc


class TemplatePage(BasePage):
    page_url = '/login'

    def registr(self, email, passw):
        self.find(login_loc.email).send_keys(email)
        self.find(login_loc.passw).send_keys(passw)
        self.find(login_loc.login_btn).click()

    def click_page(self):
        return self.find(loc.page).click()

    def add_template(self, name, description):
        self.find(loc.add_template_btn).click()
        self.find(loc.name_field).send_keys(name)
        self.find(loc.description_field).send_keys(description)
        self.find(loc.submit_btn).click()

    @property
    def result(self):
        return self.find(loc.res_table)

    def open_template(self):
        self.wait_until_visibility(loc.open_template)
        return self.find(loc.open_template).click()

    def delete_template(self):
        self.wait_until_visibility(loc.delete_template)
        return self.find(loc.delete_template).click()

    def new_tmp(self):
        self.wait_until_visibility(loc.add_new_template)
        return self.find(loc.add_new_template).click()

    def create_tmp(self, new_name):
        self.find(loc.new_name).send_keys(new_name)
        self.find(loc.add_btn).click()
        self.wait_until_visibility(workout_log_loc.exercise)
        self.find(workout_log_loc.exercise).click()
        self.wait_until_visibility(workout_log_loc.checkbox_1)
        self.find(workout_log_loc.checkbox_1).click()
        self.find(workout_log_loc.checkbox_2).click()
        return self.find(workout_log_loc.submit_btn).click()

    def submit_new_tmp(self):
        return self.find(loc.submit_new).click()

    def open_template_2(self):
        self.wait_until_visibility(loc.open_template_2)
        return self.find(loc.open_template_2).click()

    @property
    def result_2(self):
        return self.find(loc.res_table_2)
