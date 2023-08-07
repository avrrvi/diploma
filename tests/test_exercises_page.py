from pages.exercises_page import ExercisesPage


def test_1(driver):
    title = ExercisesPage(driver)
    title.open_page()
    title.registr('a@gmail.com', 'a')
    title.click_page()
    assert driver.title == 'GymPad - Упражнения'


def test_2(driver):
    click_btns = ExercisesPage(driver)
    click_btns.open_page()
    click_btns.registr('a@gmail.com', 'a')
    click_btns.click_page()
    click_btns.click_catalog()
    for exs in click_btns.click_exs:
        assert exs.is_displayed()


def test_3(driver):
    add_fav_ex = ExercisesPage(driver)
    add_fav_ex.open_page()
    add_fav_ex.registr('a@gmail.com', 'a')
    add_fav_ex.click_page()
    add_fav_ex.click_catalog()
    add_fav_ex.click_exs[2].click()
    for ex in add_fav_ex.choose_fav[::5]:
        ex.click()
    add_fav_ex.open_fav.click()
    exs_1 = 'Попеременные сгибания рук с гантелями'
    exs_2 = 'Сгибание рук на тренажере Larry Scottа'
    exs_3 = 'Сгибание рук с рукоятками верхних блоков'
    assert exs_1 or exs_2 or exs_3 in add_fav_ex.result_table.text


def test_4(driver):
    search = ExercisesPage(driver)
    search.open_page()
    search.registr('a@gmail.com', 'a')
    search.click_page()
    search_text = 'жим'
    search.search(search_text)
    for el in search.search_res:
        assert search_text in el.text.lower()
