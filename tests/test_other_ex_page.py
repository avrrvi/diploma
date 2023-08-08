from pages.template_page import TemplatePage
import allure


@allure.feature('Other Exercises Page')
@allure.story('page title')
def test_1_title(driver):
    title = TemplatePage(driver)
    with allure.step('Open LogIn page'):
        title.open_page()
    with allure.step('LogIn'):
        title.registr('a@gmail.com', 'a')
    with allure.step('Open Other Exercises page'):
        title.click_page()
    assert driver.title == 'GymPad - дневник твоих тренировок'


@allure.story('add template')
def test_2_add_tmp(driver):
    add_template = TemplatePage(driver)
    with allure.step('Open LogIn page'):
        add_template.open_page()
    with allure.step('LogIn'):
        add_template.registr('a@gmail.com', 'a')
    with allure.step('Open Other Exercises page'):
        add_template.click_page()
    with allure.step('Enter datas'):
        name = 'aaa'
        description = 'aaa'
        add_template.add_template(name, description)
    assert name.capitalize() in add_template.result.text


@allure.story('delete template')
def test_3_delete_tmp(driver):
    del_template = TemplatePage(driver)
    with allure.step('Open LogIn page'):
        del_template.open_page()
    with allure.step('LogIn'):
        del_template.registr('a@gmail.com', 'a')
    with allure.step('Open Other Exercises page'):
        del_template.click_page()
    with allure.step('Enter datas'):
        name = 'abvg'
        description = 'abvg'
        del_template.add_template(name, description)
    with allure.step('Open Template page'):
        del_template.open_template()
    with allure.step('Delete Template page'):
        del_template.scroll(pix=2000)
        del_template.delete_template()
    assert name not in del_template.result.text


@allure.story('add additional template')
def test_4_add_new_tmp(driver):
    add_new_tmp = TemplatePage(driver)
    with allure.step('Open LogIn page'):
        add_new_tmp.open_page()
    with allure.step('LogIn'):
        add_new_tmp.registr('a@gmail.com', 'a')
    with allure.step('Open Other Exercises page'):
        add_new_tmp.click_page()
    with allure.step('Enter datas'):
        name = 'aaa'
        description = 'aaa'
        add_new_tmp.add_template(name, description)
    with allure.step('Open New Template page'):
        add_new_tmp.open_template()
        add_new_tmp.new_tmp()
    with allure.step('Enter datas'):
        new_name = '111'
        add_new_tmp.create_tmp(new_name)
        add_new_tmp.submit_new_tmp()
    with allure.step('Open Templates'):
        add_new_tmp.open_template()
        add_new_tmp.open_template_2()
    assert new_name in add_new_tmp.result_2.text
