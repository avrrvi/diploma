from pages.template_page import TemplatePage


def test_1(driver):
    title = TemplatePage(driver)
    title.open_page()
    title.registr('a@gmail.com', 'a')
    title.click_page()
    assert driver.title == 'GymPad - дневник твоих тренировок'


def test_2(driver):
    add_template = TemplatePage(driver)
    add_template.open_page()
    add_template.registr('a@gmail.com', 'a')
    add_template.click_page()
    name = 'aaa'
    description = 'aaa'
    add_template.add_template(name, description)
    assert name.capitalize() in add_template.result.text


def test_3(driver):
    del_template = TemplatePage(driver)
    del_template.open_page()
    del_template.registr('a@gmail.com', 'a')
    del_template.click_page()
    name = 'abvg'
    description = 'abvg'
    del_template.add_template(name, description)
    del_template.open_template()
    del_template.delete_template()
    assert name not in del_template.result.text


def test_4(driver):
    add_new_tmp = TemplatePage(driver)
    add_new_tmp.open_page()
    add_new_tmp.registr('a@gmail.com', 'a')
    add_new_tmp.click_page()
    name = 'aaa'
    description = 'aaa'
    add_new_tmp.add_template(name, description)
    add_new_tmp.open_template()
    add_new_tmp.new_tmp()
    new_name = '111'
    add_new_tmp.create_tmp(new_name)
    add_new_tmp.submit_new_tmp()
    add_new_tmp.open_template()
    add_new_tmp.open_template_2()
    assert new_name in add_new_tmp.result_2.text



