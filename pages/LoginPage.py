from selenium.webdriver.common.by import By
from utils.logger import get_logger


class LoginPage:

    # 1. THE CONSTRUCTOR
    def __init__(self, driver):
        # Save the steering wheel so all methods in this class can use it
        self.driver = driver
        # Initialize the logger specifically for this page
        self.log = get_logger("LoginPage")

    # 2. THE LOCATORS (Stored as Tuples)
    # If UI changes, we ONLY update these three lines!
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".oxd-button.orangehrm-login-button")

    # 3. THE ACTIONS
    def enter_username(self, username):
        # self.driver steers. find_element looks at our locator. send_keys types.
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.log.info("Clicking the login button")
        self.driver.find_element(*self.LOGIN_BUTTON).click()

#(Notice the * inside find_element(*self.USERNAME_INPUT).
# Our locator is a Tuple (two items). The * just unzips
# the tuple so Selenium can read both the 'By.NAME' and the 'username' separately.)
