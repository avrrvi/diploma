from pages.home_page import HomePage
from pages.results import ResultPage
import allure


@allure.feature('Home Page')
@allure.story('page title')
def test_1_title(driver):
    home_title = HomePage(driver)
    with allure.step('Open Home page'):
        home_title.open_page()
        home_title.wait()
    assert home_title.main_title().startswith('БЕСПЛАТНЫЙ ОНЛАЙН')


@allure.story('clickable button')
def test_2_clickable(driver):
    clicked_marks = HomePage(driver)
    clicked_marks.open_page()
    for el in clicked_marks.menu_button():
        assert el.is_displayed()


@allure.story('links')
def test_3_links(driver):
    link_menu = HomePage(driver)
    link_menu.open_page()
    for link in link_menu.menu_link:
        link.click()
        result_link = ResultPage(driver).curr_page_url
        assert driver.current_url == result_link


@allure.story('click logo')
def test_4_logo(driver):
    logo = HomePage(driver)
    with allure.step('Open LogIn page'):
        logo.open_page()
    with allure.step('Click to logo'):
        logo.click_logo()
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res
