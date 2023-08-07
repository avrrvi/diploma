from pages.sign_up_page import SignUpPage
from pages.results import ResultPage
import datetime
from translate import Translator


def test_1(driver):
    page_title = SignUpPage(driver)
    page_title.open_page()
    assert page_title.main_title.text == 'GymPad - Регистрация'


def test_2(driver):
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


def test_3(driver):
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


def test_4(driver):
    docs = SignUpPage(driver)
    docs.open_page()
    assert docs.conditions().is_displayed()


def test_5(driver):
    docs = SignUpPage(driver)
    docs.open_page()
    docs.conditions().click()
    assert driver.current_url == ResultPage(driver).curr_page_url


def test_6(driver):
    empty_datas = SignUpPage(driver)
    empty_datas.open_page()
    empty_datas.sign_up()
    assert empty_datas.err_mess() == f'Email нужен для авторизации\nНапишите Ваше имя\nА пароль?'


def test_7(driver):
    taken_datas = SignUpPage(driver)
    taken_datas.open_page()
    taken_datas.email('avrrvi@gamil.com')
    taken_datas.fname('a')
    taken_datas.lname('a')
    taken_datas.passw('a')
    taken_datas.repeat_passw('a')
    taken_datas.sign_up()
    assert taken_datas.err_mess() == 'Емейл "avrrvi@gamil.com" уже занят.'


def test_8(driver):
    err = SignUpPage(driver)
    err.open_page()
    err.email('aa@g')
    err.fname('a')
    err.lname('a')
    err.passw('a')
    err.repeat_passw('a')
    err.sign_up()
    assert err.err_mess() == f'Емейл не является правильным E-Mail адресом.'


def test_9(driver):
    right_datas = SignUpPage(driver)
    right_datas.open_page()
    right_datas.email('11@gmail.com')
    right_datas.fname('a')
    right_datas.lname('a')
    right_datas.passw('a')
    right_datas.repeat_passw('a')
    right_datas.sign_up()
    translator = Translator(from_lang="russian", to_lang="english")
    translation = translator.translate(right_datas.acc().capitalize())
    assert translation == datetime.datetime.now().strftime('%B, %Y')
