from selenium.webdriver.common.by import By


add_workout = (By.CSS_SELECTOR, 'div[class="actions"] button[onclick="page_workout.create(4)"]'
                                '[data-loading-text="Загрузка"]')

add_workout_2 = (By.CSS_SELECTOR, 'i[class="glyphicon glyphicon-plus"]')
