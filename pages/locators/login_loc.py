from selenium.webdriver.common.by import By


title = (By.TAG_NAME, 'title')

email = (By.NAME, 'email')
passw = (By.NAME, 'password')
login_btn = (By.ID, 'login-submit')

forget_passw = (By.ID, 'login-forget-link')
or_registr = (By.XPATH, '//a[contains(text(), "зарегистрироваться на сайте")]')

checkbox = (By.ID, 'remember-me')
