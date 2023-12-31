from selenium.webdriver.common.by import By

acc_h1 = (By.ID, 'headerMonthYear')

open_catalog = (By.XPATH, '//*[@id="modalExercisesContent"]/div[2]/div/ul/li[2]/a')

add_workout = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[3]/div/div/button[1]')
add_workout_2 = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/a/i')
add_workout_3 = (By.CLASS_NAME, 'panel panel-default')

exercise = (By.CSS_SELECTOR, '#exerpedia > div:nth-child(5) > div.panel-heading > h4 > a')
checkbox_1 = (By.XPATH, '//*[@id="collapseCategory4"]/div/table/tbody/tr[1]')
checkbox_2 = (By.XPATH, '//*[@id="collapseCategory4"]/div/table/tbody/tr[2]')
submit_btn = (By.XPATH, '//*[@id="modalExercisesContent"]/div[3]/button')

res_table = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[2]/table')
comment = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/a[2]')

setting = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/div/i')
del_exercise = (By.XPATH, '//*[@id="modalMdContent"]/div[2]/div/button')

text_comment = (By.XPATH, '//*[@id="modalContent"]/div[2]/div[1]/input')
add_comment = (By.XPATH, '//*[@id="modalContent"]/div[3]/button')

additional = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/a[1]/i')
kg = (By.XPATH, '//*[@id="modalContent"]/div[2]/div[1]/input[1]')
repeat = (By.XPATH, '//*[@id="modalContent"]/div[2]/div[1]/input[2]')
next_btn = (By.XPATH, '//*[@id="modalContent"]/div[3]/button[1]')
ready_btn = (By.XPATH, '//*[@id="modalContent"]/div[3]/button[2]')
res = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[2]/table/tbody/tr[2]')

save_btn = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[3]/div/div/button[1]')
sum = (By.CSS_SELECTOR, '#linkToday > table > tbody > tr > td.middle > div.tonnage.pull-right > span')

wait_1 = (By.XPATH, '//td[3]/div/div/button[contains(text(), "Обновить")] ')
wait_2 = (By.XPATH, '//*[@id="count"][contains(text(), "0")]')
clear = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[3]/div/div/button[2]')
delete = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[3]/div/div/ul/li[5]/a')
submit_clear = (By.XPATH, '//button[starts-with(@id, "confirm-ok")]')
wait = (By.XPATH, '//*[@id="linkToday"]/table/tbody/tr/td[2]/div[3]')
cleared = (By.XPATH, '//*[@id="count"]')

calendar = (By.XPATH, '//*[@id="workoutCalendar"]/i')
day = (By.XPATH, '//*[@id="monthSelect"]/div/table/tbody/tr[3]/td[5]/a')
