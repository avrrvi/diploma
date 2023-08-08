from pages.exercises_page import ExercisesPage
import allure


@allure.feature('Exercises Page')
@allure.story('page title')
def test_1_title(driver):
    title = ExercisesPage(driver)
    with allure.step('Open LogIn page'):
        title.open_page()
    with allure.step('LogIn'):
        title.registr('a@gmail.com', 'a')
    with allure.step('Open Exercises page'):
        title.click_page()
    assert driver.title == 'GymPad - Упражнения'


@allure.story('clickable button')
def test_2_clickable(driver):
    click_btns = ExercisesPage(driver)
    with allure.step('Open LogIn page'):
        click_btns.open_page()
    with allure.step('LogIn'):
        click_btns.registr('a@gmail.com', 'a')
    with allure.step('Open Exercises page'):
        click_btns.click_page()
    with allure.step('Open catalog'):
        click_btns.click_catalog()
    for exs in click_btns.click_exs:
        assert exs.is_displayed()


@allure.story('add favorite exercise')
def test_3_add_fav(driver):
    add_fav_ex = ExercisesPage(driver)
    with allure.step('Open LogIn page'):
        add_fav_ex.open_page()
    with allure.step('LogIn'):
        add_fav_ex.registr('a@gmail.com', 'a')
    with allure.step('Open Exercises page'):
        add_fav_ex.click_page()
    with allure.step('Open catalog'):
        add_fav_ex.click_catalog()
    with allure.step('Add favorite exercise'):
        add_fav_ex.click_exs[2].click()
    for ex in add_fav_ex.choose_fav[::5]:
        ex.click()
    add_fav_ex.open_fav.click()
    exs_1 = 'Попеременные сгибания рук с гантелями'
    exs_2 = 'Сгибание рук на тренажере Larry Scottа'
    exs_3 = 'Сгибание рук с рукоятками верхних блоков'
    assert exs_1 or exs_2 or exs_3 in add_fav_ex.result_table.text


@allure.story('searching')
def test_4_search(driver):
    search = ExercisesPage(driver)
    with allure.step('Open LogIn page'):
        search.open_page()
    with allure.step('LogIn'):
        search.registr('a@gmail.com', 'a')
    with allure.step('Open Exercises page'):
        search.click_page()
    with allure.step('Open catalog'):
        search.click_catalog()
    with allure.step('Searching'):
        search_text = 'жим'
        search.search(search_text)
    for el in search.search_res:
        assert search_text in el.text.lower()
