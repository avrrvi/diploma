from pages.login_page import LogInPage
from pages.results import ResultPage


def test_1(driver):
    page_title = LogInPage(driver)
    page_title.open_page()
    assert driver.title == 'GymPad - Вход'


def test_2(driver):
    login = LogInPage(driver)
    login.open_page()
    login.datas('a@gmail.com', 'a')
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res


def test_3(driver):
    btns = LogInPage(driver)
    btns.open_page()
    assert btns.click_forget_passw.is_displayed()
    assert btns.click_login.is_displayed()
    assert btns.click_registr.is_displayed()


def test_4(driver):
    check = LogInPage(driver)
    check.open_page()
    assert check.checkbox.is_selected()
