from pages.programs_page import ProgramsPage


def test_1(driver):
    title = ProgramsPage(driver)
    title.open_page()
    title.registr('a@gmail.com', 'a')
    title.click_page()
    assert driver.title == 'GymPad - дневник твоих тренировок'


def test_2(driver):
    add_prog = ProgramsPage(driver)
    add_prog.open_page()
    add_prog.registr('a@gmail.com', 'a')
    add_prog.click_page()
    for btn in add_prog.click_btn():
        assert btn.is_displayed()


def test_3(driver):
    add_prog = ProgramsPage(driver)
    add_prog.open_page()
    add_prog.registr('a@gmail.com', 'a')
    add_prog.click_page()
    add_prog.click_btn()[0].click()
    assert driver.current_url == f'{add_prog.base_page_url}/templates'
    assert add_prog.added_tmp.text in add_prog.added_res.text

