from pages.search import SearchPage
from pages.results import ResultPage
import allure


@allure.feature('Google')
@allure.story('search in google')
def test_search_web(driver):
    search_page = SearchPage(driver)
    with allure.step('Open Google'):
        search_page.open_page()
    with allure.step('Enter datas'):
        search_page.enter_search_phrase('gympad')
    with allure.step('Opened result in Google'):
        results_page = ResultPage(driver)
    assert results_page.page_title.startswith('gympad')
