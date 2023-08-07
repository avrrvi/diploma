from pages.base_page import BasePage
from pages.locators import workout_log_loc as loc
from pages.locators import login_loc


class WorkOutPage(BasePage):
    page_url = '/login'

    def registr(self, email, passw):
        self.find(login_loc.email).send_keys(email)
        self.find(login_loc.passw).send_keys(passw)
        self.find(login_loc.login_btn).click()

    def acc(self):
        return self.find(loc.acc_h1).text

    def add_workout_btn(self):
        return self.find(loc.add_workout).click()

    def add_workout_btn_2(self):
        self.wait_until_visibility(loc.add_workout_2)
        self.find(loc.add_workout_2).click()

    def open_catalog(self):
        self.wait_until_visibility(loc.open_catalog)
        return self.find(loc.open_catalog).click()

    @property
    def add_workout_btn_3(self):
        return self.find_all(loc.add_workout_3)

    def add_exercise(self):
        self.wait_until_visibility(loc.exercise)
        self.find(loc.exercise).click()

    def click_checkboxes(self):
        self.wait_until_visibility(loc.checkbox_1)
        self.find(loc.checkbox_1).click()
        self.find(loc.checkbox_2).click()

    @property
    def submit_checks(self):
        return self.find(loc.submit_btn)

    @property
    def result_table(self):
        return self.find(loc.res_table)

    @property
    def comment(self):
        return self.find(loc.comment)

    def setting_button(self):
        return self.find(loc.setting).click()

    def delete_exercise(self):
        return self.find(loc.del_exercise).click()

    def text_comment(self, comment):
        return self.find(loc.text_comment).send_keys(comment)

    def add_comment(self):
        return self.find(loc.add_comment).click()

    def additional(self):
        return self.find(loc.additional).click()

    def add_additional(self, kg, repeat):
        self.find(loc.kg).send_keys(kg)
        self.find(loc.repeat).send_keys(repeat)

    def button_next(self):
        self.find(loc.next_btn).click()

    def button_ready(self):
        self.find(loc.ready_btn).click()

    @property
    def result(self):
        return self.find(loc.res)

    def button_save(self):
        return self.find(loc.save_btn).click()

    def sum(self):
        self.wait_until_visibility(loc.sum)
        return self.find(loc.sum).text

    def clear_all(self):
        self.wait_until_visibility(loc.clear)
        self.find(loc.clear).click()
        self.wait_until_visibility(loc.delete)
        self.find(loc.delete).click()
        self.wait_until_visibility(loc.submit_clear)
        self.find(loc.submit_clear).click()

    # @property
    def cleared(self):
        self.driver.implicitly_wait(10)
        return self.find(loc.cleared)

    def click_calendar(self):
        return self.find(loc.calendar).click()

    @property
    def choose_day(self):
        self.wait_until_visibility(loc.day)
        return self.find(loc.day)
