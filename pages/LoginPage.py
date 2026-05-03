from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.log = get_logger("LoginPage")
        # Define a standard wait time (10 seconds is usually enough)
        self.wait = WebDriverWait(self.driver, 10)

    # LOCATORS
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".oxd-button.orangehrm-login-button")

    # ACTIONS
    def enter_username(self, username):
        self.log.info(f"Entering username")
        # Wait until the element is actually visible and ready for text
        el = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        el.clear() # Best practice: clear before typing
        el.send_keys(username)

    def enter_password(self, password):
        self.log.info("Entering password")
        el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        self.log.info("Clicking the login button")
        # Wait until the button is 'Clickable' (not just present in the DOM)
        btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        btn.click()