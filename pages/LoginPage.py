from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.log = get_logger("LoginPage")
        self.wait = WebDriverWait(self.driver, 15) # Increased to 15s for CI lag

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".oxd-button.orangehrm-login-button")

    def enter_username(self, username):
        self.log.info("Entering username")
        el = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        el.clear()
        el.send_keys(username)

    def enter_password(self, password):
        self.log.info("Entering password")
        el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        self.log.info("Clicking the login button")
        btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        # JavaScript click is an SDET 'pro-move' to ensure the click fires in headless mode
        self.driver.execute_script("arguments[0].click();", btn)