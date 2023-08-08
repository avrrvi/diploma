from pages.sizes_page import SizesPage
import allure


@allure.feature('Sizes Page')
@allure.story('page title')
def test_1_title(driver):
    title = SizesPage(driver)
    with (allure.step('Open LogIn page')):
        title.open_page()
    with allure.step('LogIn'):
        title.registr('a@gmail.com', 'a')
    with allure.step('Open Sizes page'):
        title.click_page()
    assert driver.title == 'GymPad - Замеры'
