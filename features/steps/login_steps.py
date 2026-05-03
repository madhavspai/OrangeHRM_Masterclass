from behave import given, when, then
from pages.LoginPage import LoginPage
import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@given('I navigate to the OrangeHRM login page')
def step_navigate_to_login(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('I enter valid credentials')
def step_enter_credentials(context):
    login_page = LoginPage(context.driver)
    with allure.step(f"Typing username: {test_data.VALID_USERNAME}"):
        login_page.enter_username(test_data.VALID_USERNAME)
    with allure.step("Typing secure password"):
        login_page.enter_password(test_data.VALID_PASSWORD)

@when('I click the login button')
def step_click_login(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()

@then('I should be logged in successfully')
def step_verify_login(context):
    # Increased timeout to 20s to account for slow CI server response
    WebDriverWait(context.driver, 20).until(
        EC.url_contains("dashboard"),
        message="Login failed: Dashboard URL did not load within 20 seconds"
    )
    assert "dashboard" in context.driver.current_url.lower()