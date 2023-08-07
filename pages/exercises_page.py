from pages.base_page import BasePage
from pages.locators import exercises_loc as loc
from pages.locators import login_loc


class ExercisesPage(BasePage):
    page_url = '/login'

    def registr(self, email, passw):
        self.find(login_loc.email).send_keys(email)
        self.find(login_loc.passw).send_keys(passw)
        self.find(login_loc.login_btn).click()

    def click_page(self):
        return self.find(loc.page).click()

    def click_catalog(self):
        return self.find(loc.open_catalog).click()

    @property
    def click_exs(self):
        return self.find_all(loc.exercises)

    @property
    def choose_fav(self):
        self.wait_until_visibility(loc.fav_exercise)
        return self.find_all(loc.fav_exercise)

    @property
    def open_fav(self):
        return self.find(loc.open_fav)

    @property
    def result_table(self):
        return self.find(loc.res_table)

    def search(self, search_txt):
        self.find(loc.search_field).click()
        return self.find(loc.search_text).send_keys(search_txt)

    @property
    def search_res(self):
        self.wait_until_visibility(loc.search_result)
        return self.find_all(loc.search_result)

