from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    google_url = 'https://www.google.com'
    base_page_url = 'https://www.gympad.ru'
    google_page_url = None
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.google_page_url:
            self.driver.get(f'{self.google_url}{self.google_page_url}')
        elif self.page_url:
            self.driver.get(f'{self.base_page_url}{self.page_url}')
        else:
            raise NotImplementedError('This page cannot be opened by URL')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def scroll(self, pix=None):
        if not pix:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            self.driver.execute_script(f"window.scrollTo(0, {pix});")

    def wait_until_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

