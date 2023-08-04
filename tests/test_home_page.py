from pages.home_page import HomePage
from pages.results import ResultPage


def test_1(driver):
    home_title = HomePage(driver)
    home_title.open_page()
    home_title.wait()
    assert home_title.main_title().startswith('БЕСПЛАТНЫЙ ОНЛАЙН')


def test_2(driver):
    clicked_marks = HomePage(driver)
    clicked_marks.open_page()
    for el in clicked_marks.menu_button():
        assert el.is_displayed()


def test_3(driver):
    link_menu = HomePage(driver)
    link_menu.open_page()
    for link in link_menu.menu_link:
        link.click()
        result_link = ResultPage(driver).curr_page_url
        assert driver.current_url == result_link


def test_4(driver):
    logo = HomePage(driver)
    logo.open_page()
    logo.click_logo()
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res


# def test_5(driver):
    # btns = HomePage(driver)
    # btns.open_page()
    # btns.wait()
    # btns.scroll()
    # for buttons in btns.clickable_btns():
    #     assert buttons.is_displayed()


# def test_5_search_field(driver):
#     search = HomePage(driver)
#     search.open_page()
#     search.enter_search_phrase('what? where? when?')
#     res = ResultPage(driver).curr_page_url
#     assert driver.current_url == res
