from pages.sign_up_page import SignUpPage
from pages.results import ResultPage
import allure


@allure.feature('SignUp Page')
@allure.story('page title')
def test_1_title(driver):
    page_title = SignUpPage(driver)
    page_title.open_page()
    assert driver.title == 'GymPad - Регистрация'


@allure.story('clickable button')
def test_2_socialmedia_btn(driver):
    socialmedia = SignUpPage(driver)
    socialmedia.open_page()
    vk = socialmedia.signup_by_vk
    apple = socialmedia.signup_by_apple
    yandex = socialmedia.signup_by_yandex
    google = socialmedia.signup_by_google
    assert vk.is_displayed()
    assert apple.is_displayed()
    assert yandex.is_displayed()
    assert google.is_displayed()


@allure.story('links')
def test_3_socialmedia_links(driver):
    socialmedia_link = SignUpPage(driver)
    socialmedia_link.open_page()
    socialmedia_link.vk_link()
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res
    socialmedia_link.open_page()
    socialmedia_link.apple_link()
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res
    socialmedia_link.open_page()
    socialmedia_link.yandex_link()
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res
    socialmedia_link.open_page()
    socialmedia_link.google_link()
    res = ResultPage(driver).curr_page_url
    assert driver.current_url == res


@allure.story('clickable button')
def test_4_conditions_btn(driver):
    docs = SignUpPage(driver)
    docs.open_page()
    assert docs.conditions().is_displayed()


@allure.story('links')
def test_5_conditions_link(driver):
    docs = SignUpPage(driver)
    with allure.step('Open SugnUp page'):
        docs.open_page()
    with allure.step('Open Conditions page'):
        docs.conditions().click()
    assert driver.current_url == ResultPage(driver).curr_page_url


@allure.story('error message')
def test_6_err_mes_of_empty(driver):
    empty_datas = SignUpPage(driver)
    with allure.step('Open SugnUp page'):
        empty_datas.open_page()
    with allure.step('Sign Up with empty datas'):
        empty_datas.sign_up()
    assert empty_datas.err_mess() == f'Email нужен для авторизации\nНапишите Ваше имя\nА пароль?'


@allure.story('error message')
def test_7_existing_email_err(driver):
    taken_datas = SignUpPage(driver)
    with allure.step('Open SignUp page'):
        taken_datas.open_page()
    with allure.step('Enter datas'):
        taken_datas.email('avrrvi@gamil.com')
        taken_datas.fname('a')
        taken_datas.lname('a')
        taken_datas.passw('a')
        taken_datas.repeat_passw('a')
        taken_datas.sign_up()
    assert taken_datas.err_mess() == 'Емейл "avrrvi@gamil.com" уже занят.'


@allure.story('error message')
def test_8_email_err_mess(driver):
    err = SignUpPage(driver)
    with allure.step('Open SignUp page'):
        err.open_page()
    with allure.step('Enter datas'):
        err.email('aa@g')
        err.fname('a')
        err.lname('a')
        err.passw('a')
        err.repeat_passw('a')
        err.sign_up()
    assert err.err_mess() == f'Емейл не является правильным E-Mail адресом.'
