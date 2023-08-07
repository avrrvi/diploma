from pages.workout_log_page import WorkOutPage


def test_1(driver):
    click_btn = WorkOutPage(driver)
    click_btn.open_page()
    click_btn.registr('a@gmail.com', 'a')
    click_btn.add_workout_btn()
    click_btn.add_workout_btn_2()
    for el in click_btn.add_workout_btn_3:
        assert el.is_displayed()


def test_2(driver):
    add_workout = WorkOutPage(driver)
    add_workout.open_page()
    add_workout.registr('a@gmail.com', 'a')
    add_workout.clear_all()
    add_workout.add_workout_btn()
    add_workout.add_workout_btn_2()
    add_workout.add_exercise()
    add_workout.click_checkboxes()
    add_workout.submit_checks.click()
    add_workout.setting_button()
    add_workout.delete_exercise()
    ex = 'Разгибание запястий со штангой хватом сверху'
    assert ex not in add_workout.result_table.text


def test_3(driver):
    add_workout = WorkOutPage(driver)
    add_workout.open_page()
    add_workout.registr('a@gmail.com', 'a')
    add_workout.add_workout_btn()
    add_workout.add_workout_btn_2()
    add_workout.add_exercise()
    add_workout.click_checkboxes()
    add_workout.submit_checks.click()
    ex_1 = 'Сгибание запястий со штангой хватом снизу'
    ex_2 = 'Разгибание запястий со штангой хватом сверху'
    assert ex_1 and ex_2 in add_workout.result_table.text


def test_4(driver):
    comment_workout = WorkOutPage(driver)
    comment_workout.open_page()
    comment_workout.registr('a@gmail.com', 'a')
    comment_workout.add_workout_btn()
    comment_workout.add_workout_btn_2()
    comment_workout.add_exercise()
    comment_workout.click_checkboxes()
    comment_workout.submit_checks.click()
    comment_workout.comment.click()
    comment_workout.text_comment('Очень важно!')
    comment_workout.add_comment()
    assert 'Очень важно!' in comment_workout.result_table.text


def test_5(driver):
    additional_info = WorkOutPage(driver)
    additional_info.open_page()
    additional_info.registr('a@gmail.com', 'a')
    additional_info.add_workout_btn()
    additional_info.add_workout_btn_2()
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


def test_6(driver):
    clear = WorkOutPage(driver)
    clear.open_page()
    clear.registr('a@gmail.com', 'a')
    clear.clear_all()
    assert clear.cleared.text == 'Тренировка не записана'


def test_7(driver):
    save = WorkOutPage(driver)
    save.open_page()
    save.registr('a@gmail.com', 'a')
    save.add_workout_btn()
    save.add_workout_btn_2()
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



