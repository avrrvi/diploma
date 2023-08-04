from pages.base_page import BasePage
from pages.locators import search_loc as loc


class SearchPage(BasePage):
    google_page_url = '/'

    def enter_search_phrase(self, phrase):
        search = self.find(loc.search_field)
        search.send_keys(phrase)
        search.submit()
