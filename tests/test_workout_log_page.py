from pages.workout_log_page import WorkOutPage
import datetime
from translate import Translator
from time import sleep
import allure


@allure.feature('Workout Log Page')
@allure.story('page title')
def test_1_title(driver):
    title = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        title.open_page()
    with allure.step('LogIn'):
        title.registr('a@gmail.com', 'a')
    assert driver.title == 'GymPad - Тренировки'


@allure.story('page date')
def test_2_date(driver):
    right_datas = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        right_datas.open_page()
    with allure.step('LogIn'):
        right_datas.registr('a@gmail.com', 'a')
    translator = Translator(from_lang="russian", to_lang="english")
    translation = translator.translate(right_datas.acc().capitalize())
    assert translation == datetime.datetime.now().strftime('%B, %Y')


@allure.story('clickable button')
def test_3_catalog_btns(driver):
    click_btn = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        click_btn.open_page()
    with allure.step('LogIn'):
        click_btn.registr('a@gmail.com', 'a')
    with allure.step('Add workouts'):
        click_btn.add_workout_btn()
        click_btn.add_workout_btn_2()
        click_btn.open_catalog()
    for el in click_btn.add_workout_btn_3:
        assert el.is_displayed()


@allure.story('delete workout')
def test_4_delete_workout(driver):
    add_workout = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        add_workout.open_page()
    with allure.step('LogIn'):
        add_workout.registr('a@gmail.com', 'a')
    with allure.step('Add workouts'):
        add_workout.add_workout_btn()
        add_workout.add_workout_btn_2()
        add_workout.open_catalog()
        add_workout.add_exercise()
        add_workout.click_checkbox()
        add_workout.submit_checks.click()
    with allure.step('Delete workouts'):
        add_workout.setting_button()
        add_workout.delete_exercise()
    with allure.step('Save changes'):
        add_workout.button_save()
    ex = 'Сгибание запястий со штангой хватом снизу'
    assert ex not in add_workout.result_table.text


@allure.story('add workout')
def test_5_add_workout(driver):
    add_workout = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        add_workout.open_page()
    with allure.step('LogIn'):
        add_workout.registr('a@gmail.com', 'a')
    with allure.step('Add workouts'):
        add_workout.add_workout_btn()
        add_workout.add_workout_btn_2()
        add_workout.open_catalog()
        add_workout.add_exercise()
        add_workout.click_checkbox()
        add_workout.submit_checks.click()
    ex = 'Сгибание запястий со штангой хватом снизу'
    assert ex in add_workout.result_table.text


@allure.story('comment workout')
def test_6_add_comment(driver):
    comment_workout = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        comment_workout.open_page()
    with allure.step('LogIn'):
        comment_workout.registr('a@gmail.com', 'a')
    with allure.step('Add workouts'):
        comment_workout.add_workout_btn()
        comment_workout.add_workout_btn_2()
        comment_workout.open_catalog()
        comment_workout.add_exercise()
        comment_workout.click_checkbox()
        comment_workout.submit_checks.click()
    with allure.step('Add comment to workout'):
        comment_workout.comment.click()
        comment_workout.text_comment('Очень важно!')
        comment_workout.add_comment()
    assert 'Очень важно!' in comment_workout.result_table.text


@allure.story('additional info')
def test_7_add_additional_info(driver):
    additional_info = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        additional_info.open_page()
    with allure.step('LogIn'):
        additional_info.registr('a@gmail.com', 'a')
    with allure.step('Add workouts'):
        additional_info.add_workout_btn()
        additional_info.add_workout_btn_2()
        additional_info.open_catalog()
        additional_info.add_exercise()
        additional_info.click_checkbox()
        additional_info.submit_checks.click()
    with allure.step('Add additional info'):
        additional_info.additional()
        additional_info.add_additional(2, 2)
        additional_info.button_next()
        additional_info.add_additional(3, 3)
        additional_info.button_ready()
    with allure.step('Save changes'):
        additional_info.button_save()
    assert '2', '3' in additional_info.result.text


@allure.story('sum workouts')
def test_8_sum_workouts(driver):
    save = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        save.open_page()
    with allure.step('LogIn'):
        save.registr('a@gmail.com', 'a')
    save.clear_all()
    with allure.step('Add workouts'):
        save.add_workout_btn()
        save.add_workout_btn_2()
        save.open_catalog()
        save.add_exercise()
        save.click_checkbox()
        save.submit_checks.click()
    with allure.step('Add comment to workout'):
        save.comment.click()
        save.text_comment('Очень важно!')
        save.add_comment()
    with allure.step('Add additional info'):
        save.additional()
        save.add_additional(2, 2)
        save.button_next()
        save.add_additional(3, 3)
        save.button_ready()
    with allure.step('Save changes'):
        save.button_save()
    assert save.sum() == '13'


@allure.story('clear all')
def test_9_clear(driver):
    clear = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        clear.open_page()
    with allure.step('LogIn'):
        clear.registr('a@gmail.com', 'a')
    with allure.step('Clear all'):
        clear.clear_all()
        sleep(3)
    assert clear.cleared().text == '0'


@allure.story('choose day')
def test_10_choose_day(driver):
    calendar = WorkOutPage(driver)
    with allure.step('Open LogIn page'):
        calendar.open_page()
    with allure.step('LogIn'):
        calendar.registr('a@gmail.com', 'a')
    with allure.step('Choose day'):
        calendar.click_calendar()
        calendar.choose_day.click()
    assert driver.current_url == f'{calendar.base_page_url}/workouts/month/8/year/2023/day/18'
