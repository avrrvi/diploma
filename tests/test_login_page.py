from pages.login_page import LogInPage
from pages.results import ResultPage
import allure


@allure.feature('LogIn Page')
@allure.story('page title')
def test_1_title(driver):
    page_title = LogInPage(driver)
    page_title.open_page()
    assert driver.title == 'GymPad - Вход'


@allure.story('log in')
def test_2_login(driver):
    login = LogInPage(driver)
    with allure.step('Open LogIn page'):
        login.open_page()
    with allure.step('LogIn'):
        login.datas('a@gmail.com', 'a')
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res


@allure.story('clickable button')
def test_3_clickable(driver):
    btns = LogInPage(driver)
    btns.open_page()
    assert btns.click_forget_passw.is_displayed()
    assert btns.click_login.is_displayed()
    assert btns.click_registr.is_displayed()


@allure.story('seleting')
def test_4_select(driver):
    check = LogInPage(driver)
    check.open_page()
    assert check.checkbox.is_selected()
