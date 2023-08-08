from pages.nutrition_page import NutritionPage
import random
import allure


@allure.feature('Nutrition Page')
@allure.story('page title')
def test_1_title(driver):
    title = NutritionPage(driver)
    with allure.step('Open LogIn page'):
        title.open_page()
    with allure.step('LogIn'):
        title.registr('a@gmail.com', 'a')
    with allure.step('Open Nutrition page'):
        title.click_page()
    assert driver.title == 'GymPad - Дневник питания'


@allure.story('add pfc datas')
def test_2_add_pfc(driver):
    add_nutrition = NutritionPage(driver)
    with allure.step('Open LogIn page'):
        add_nutrition.open_page()
    with allure.step('LogIn'):
        add_nutrition.registr('a@gmail.com', 'a')
    with allure.step('Open Nutrition page'):
        add_nutrition.click_page()
    with allure.step('Select day'):
        add_nutrition.click_day()
    with allure.step('Enter datas'):
        name = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        prot = random.randint(10, 300)
        fats = random.randint(10, 300)
        carboh = random.randint(10, 300)
        cal = random.randint(10, 300)
        weight = random.randint(10, 300)
        add_nutrition.input_data(name, prot, fats, carboh, cal, weight)
        add_nutrition.click_add_btn()
    assert (name and str(prot) and str(fats)
            and str(carboh) and str(cal) and str(weight) in add_nutrition.result_table().text)
    for el in add_nutrition.total():
        assert el != '0'
    with allure.step('Delete added field'):
        add_nutrition.del_field()
