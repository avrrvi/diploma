from selenium.webdriver.common.by import By


page = (By.XPATH, '//*[@id="sidebar-nav"]/ul/li[3]/a')
exercises = (By.XPATH, '//*[@id="exerpedia"]/div')
fav_exercise = (By.XPATH, '//*[@id="collapseCategory3"]/div/table/tbody/tr/td[2]/a/i')
open_fav = (By.XPATH, '//*[@id="exercises"]/div[1]/div/div/div/ul/li[1]/a')
open_catalog = (By.XPATH, '//*[@id="exercises"]/div[1]/div/div/div/ul/li[2]/a')
res_table = (By.XPATH, '//*[@id="exercises"]/div[1]/div/div/div/div')

search_field = (By.XPATH, '//*[@id="exercises"]/div[1]/div/div/div/ul/li[4]/a')
search_text = (By.XPATH, '//*[@id="searchBlock"]/div/div/input')
search_result = (By.XPATH, '//*[@id="searchResult"]/tbody/tr')
