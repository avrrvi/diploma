from pages.workout_log_page import WorkOutPage
import datetime
from translate import Translator
from time import sleep


def test_1(driver):
    title = WorkOutPage(driver)
    title.open_page()
    title.registr('a@gmail.com', 'a')
    assert driver.title == 'GymPad - Тренировки'


def test_2(driver):
    right_datas = WorkOutPage(driver)
    right_datas.open_page()
    right_datas.registr('a@gmail.com', 'a')
    translator = Translator(from_lang="russian", to_lang="english")
    translation = translator.translate(right_datas.acc().capitalize())
    assert translation == datetime.datetime.now().strftime('%B, %Y')


def test_3(driver):
    click_btn = WorkOutPage(driver)
    click_btn.open_page()
    click_btn.registr('a@gmail.com', 'a')
    click_btn.add_workout_btn()
    click_btn.add_workout_btn_2()
    click_btn.open_catalog()
    for el in click_btn.add_workout_btn_3:
        assert el.is_displayed()


def test_4(driver):
    add_workout = WorkOutPage(driver)
    add_workout.open_page()
    add_workout.registr('a@gmail.com', 'a')
    add_workout.add_workout_btn()
    add_workout.add_workout_btn_2()
    add_workout.open_catalog()
    add_workout.add_exercise()
    add_workout.click_checkboxes()
    add_workout.submit_checks.click()
    add_workout.setting_button()
    add_workout.delete_exercise()
    add_workout.button_save()
    ex = 'Сгибание запястий со штангой хватом снизу'
    assert ex not in add_workout.result_table.text


def test_5(driver):
    add_workout = WorkOutPage(driver)
    add_workout.open_page()
    add_workout.registr('a@gmail.com', 'a')
    add_workout.add_workout_btn()
    add_workout.add_workout_btn_2()
    add_workout.open_catalog()
    add_workout.add_exercise()
    add_workout.click_checkboxes()
    add_workout.submit_checks.click()
    ex_1 = 'Сгибание запястий со штангой хватом снизу'
    ex_2 = 'Разгибание запястий со штангой хватом сверху'
    assert ex_1 and ex_2 in add_workout.result_table.text


def test_6(driver):
    comment_workout = WorkOutPage(driver)
    comment_workout.open_page()
    comment_workout.registr('a@gmail.com', 'a')
    comment_workout.add_workout_btn()
    comment_workout.add_workout_btn_2()
    comment_workout.open_catalog()
    comment_workout.add_exercise()
    comment_workout.click_checkboxes()
    comment_workout.submit_checks.click()
    comment_workout.comment.click()
    comment_workout.text_comment('Очень важно!')
    comment_workout.add_comment()
    assert 'Очень важно!' in comment_workout.result_table.text


def test_7(driver):
    additional_info = WorkOutPage(driver)
    additional_info.open_page()
    additional_info.registr('a@gmail.com', 'a')
    additional_info.add_workout_btn()
    additional_info.add_workout_btn_2()
    additional_info.open_catalog()
    additional_info.add_exercise()
    additional_info.click_checkboxes()
    additional_info.submit_checks.click()
    additional_info.additional()
    additional_info.add_additional(2, 2)
    additional_info.button_next()
    additional_info.add_additional(3, 3)
    additional_info.button_ready()
    additional_info.button_save()
    assert '2', '3' in additional_info.result.text


def test_8(driver):
    save = WorkOutPage(driver)
    save.open_page()
    save.registr('a@gmail.com', 'a')
    save.clear_all()
    save.add_workout_btn()
    save.add_workout_btn_2()
    save.open_catalog()
    save.add_exercise()
    save.click_checkboxes()
    save.submit_checks.click()
    save.comment.click()
    save.text_comment('Очень важно!')
    save.add_comment()
    save.additional()
    save.add_additional(2, 2)
    save.button_next()
    save.add_additional(3, 3)
    save.button_ready()
    save.button_save()
    assert save.sum() == '13'


def test_9(driver):
    clear = WorkOutPage(driver)
    clear.open_page()
    clear.registr('a@gmail.com', 'a')
    clear.clear_all()
    sleep(3)
    assert clear.cleared().text == '0'


def test_10(driver):
    calendar = WorkOutPage(driver)
    calendar.open_page()
    calendar.registr('a@gmail.com', 'a')
    calendar.click_calendar()
    calendar.choose_day.click()
    assert driver.current_url == f'{calendar.base_page_url}/workouts/month/8/year/2023/day/18'
