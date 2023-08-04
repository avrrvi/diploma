from pages.base_page import BasePage


class ResultPage(BasePage):
    page_url = None

    @property
    def page_title(self):
        return self.driver.title

    @property
    def curr_page_url(self):
        return self.driver.current_url
