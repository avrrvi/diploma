from pages.programs_page import ProgramsPage
import allure


@allure.feature('Program Page')
@allure.story('page title')
def test_1_title(driver):
    title = ProgramsPage(driver)
    with allure.step('Open LogIn page'):
        title.open_page()
    with allure.step('LogIn'):
        title.registr('a@gmail.com', 'a')
    with allure.step('Open Program page'):
        title.click_page()
    assert driver.title == 'GymPad - дневник твоих тренировок'


@allure.story('clickable button')
def test_2_add_prog_btn(driver):
    add_prog = ProgramsPage(driver)
    with allure.step('Open LogIn page'):
        add_prog.open_page()
    with allure.step('LogIn'):
        add_prog.registr('a@gmail.com', 'a')
    with allure.step('Open Program page'):
        add_prog.click_page()
    for btn in add_prog.click_btn():
        assert btn.is_displayed()


@allure.story('add exercises program')
def test_3_add_prog(driver):
    add_prog = ProgramsPage(driver)
    with allure.step('Open LogIn page'):
        add_prog.open_page()
    with allure.step('LogIn'):
        add_prog.registr('a@gmail.com', 'a')
    with allure.step('Open Program page'):
        add_prog.click_page()
    with allure.step('Add exercises program'):
        add_prog.click_btn()[0].click()
    assert driver.current_url == f'{add_prog.base_page_url}/templates'
    assert add_prog.added_tmp.text in add_prog.added_res.text
