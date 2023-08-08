from pages.nutrition_page import NutritionPage


def test_1(driver):
    title = NutritionPage(driver)
    title.open_page()
    title.registr('a@gmail.com', 'a')
    title.click_page()
    assert driver.title == 'GymPad - Дневник питания'


def test_2(driver):
    add_nutrition = NutritionPage(driver)
    add_nutrition.open_page()
    add_nutrition.registr('a@gmail.com', 'a')
    add_nutrition.click_page()
