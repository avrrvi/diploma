from selenium.webdriver.common.by import By


page = (By.XPATH, '//*[@id="sidebar-nav"]/ul/li[5]/a/span')

choose_day = (By.XPATH, '//*[@id="nutritionCalendarBlock"]/div/div/table/tbody/tr[3]/td[5]/a')

text_name = (By.XPATH, '//*[@id="nutInput"]')
text_proteins = (By.XPATH, '//*[@id="nutProtInput"]')
text_fats = (By.XPATH, '//*[@id="nutFatInput"]')
text_carbohydrates = (By.XPATH, '//*[@id="nutCarbInput"]')
text_cal = (By.XPATH, '//*[@id="nutCalInput"]')
text_weight = (By.XPATH, '//*[@id="nutWeightInput"]')
add_btn = (By.XPATH, '//*[@id="nutSubmit"]')

res_table = (By.XPATH, '//*[@id="nutrition"]/div[2]/div/div/ul/li')
wait = (By.XPATH, '//*[@id="nutrition"]/div[2]/div/div/ul/li/a/i')
total = (By.XPATH, '//*[starts-with(@id, "total")]')
