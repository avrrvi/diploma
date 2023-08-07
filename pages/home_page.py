from pages.base_page import BasePage
from pages.locators import home_loc as loc


class HomePage(BasePage):
    page_url = '/'

    def main_title(self):
        return self.find(loc.main_title).text

    def menu_button(self):
        return self.find_all(loc.menu)

    @property
    def menu_link(self):
        return self.find_all(loc.menu)

    def click_logo(self):
        self.find(loc.logo).click()

    def wait(self):
        self.wait_until_visibility(loc.main_title)
