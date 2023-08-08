from pages.nutrition_page import NutritionPage


def test_1(driver):
    title = NutritionPage(driver)
    title.open_page()
    title.registr('a@gmail.com', 'a')
    title.click_page()
    assert driver.title == 'GymPad - Дневник питания'
