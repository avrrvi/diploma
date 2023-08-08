from pages.nutrition_page import NutritionPage
import random
from time import sleep


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
    add_nutrition.click_day()
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
    add_nutrition.del_field()
