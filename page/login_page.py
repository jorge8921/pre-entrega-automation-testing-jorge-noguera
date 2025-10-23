#page/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

class LoginPage:
    _INPUT_NAME = (By.ID, "user-name")
    _INPUT_PASSWORD = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username="standard_user", password="secret_sauce"):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()
