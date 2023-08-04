from selenium.webdriver.common.by import By


title = (By.XPATH, '//title')

text_of_selector = '.ulogin-button-'
signup_by_vk = (By.CSS_SELECTOR, f'{text_of_selector}vkontakte')
signup_by_fb = (By.CSS_SELECTOR, f'{text_of_selector}facebook')
signup_by_google = (By.CSS_SELECTOR, f'{text_of_selector}google')
signup_by_odnoklassniki = (By.CSS_SELECTOR, f'{text_of_selector}odnoklassniki')

doc = (By.XPATH, '//a[contains(text(), "Оферты")]')

email = (By.NAME, 'email')
fname = (By.NAME, 'first_name')
lname = (By.NAME, 'last_name')
password = (By.NAME, 'new_password')
confirm_password = (By.NAME, 'new_repeat_password')
sign_up = (By.ID, 'registration-submit')

wait_loc = (By.CLASS_NAME, 'notice')
empty_err_mess = (By.CSS_SELECTOR, '.alert.alert-danger.alert-login')

acc_title = (By.ID, 'headerMonthYear')
