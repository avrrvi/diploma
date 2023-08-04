from pages.workout_log_page import WorkOutPage
from pages.results import ResultPage


def test_1(driver):
    click_btn = WorkOutPage(driver)
    click_btn.open_page()
    click_btn.registr('a@gmail.com', 'a')
    click_btn.add_workout_btn.click()
    # click_btn.wait()
    click_btn.add_workout_btn_2.click()

