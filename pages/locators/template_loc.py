from selenium.webdriver.common.by import By


page = (By.XPATH, '//*[@id="sidebar-nav"]/ul/li[2]/a')

open_catalog = (By.XPATH, '//*[@id="modalExercisesContent"]/div[2]/div/ul/li[2]/a')

add_template_btn = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div/div[2]/div/div/div[2]/div/a')
name_field = (By.XPATH, '//*[@id="f_name"]')
description_field = (By. XPATH, '//*[@id="f_description"]')
submit_btn = (By.XPATH, '//*[@id="template"]/fieldset/div[3]/div/button')

res_table = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div/div[2]/div/div/div[2]')
res_table_2 = (By.XPATH, '//*[starts-with(@id, "collapse")]/div/table/tbody/tr/td/div')

open_template = (By.XPATH, '//*[@id="accordion1"]/div')
open_template_2 = (By.XPATH, '//*[starts-with(@id, "collapse")]/div/table/tbody/tr/td/div')
delete_template = (By.XPATH, '//*[starts-with(@id, "collapse")]/div/div/a[2]')

add_new_template = (By.XPATH, '//*[starts-with(@id, "collapse")]/div/a')
new_name = (By.XPATH, '//*[@id="f_name"]')
add_btn = (By.XPATH, '//*[@id="exerciseNew"]/i')
submit_new = (By.XPATH, '//*[@id="template"]/fieldset/div[3]/div/button')
popup = (By.XPATH, '//*[@id="modalExercisesContent"]')

