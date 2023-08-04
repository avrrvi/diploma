from pages.search import SearchPage
from pages.results import ResultPage


def test_search_web(driver):
    search_page = SearchPage(driver)
    search_page.open_page()
    search_page.enter_search_phrase('gympad')
    results_page = ResultPage(driver)
    assert results_page.page_title.startswith('gympad')
