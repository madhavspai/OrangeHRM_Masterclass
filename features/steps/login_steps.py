
"""If I blank out while
writing step definitions,
remember this sequence: Context -> Page Object -> Action."""

from behave import given, when, then
from pages.LoginPage import LoginPage
import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@given('I navigate to the OrangeHRM login page')
def step_navigate_to_login(context):
    # We tell the driver inside the context to open the URL
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('I enter valid credentials')
def step_enter_credentials(context):
    login_page = LoginPage(context.driver)

    # We create microscopic sub-steps for the report!
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
    # Tell the driver to pause and poll the browser for up to 10 seconds
    # until the word "dashboard" appears in the URL.
    WebDriverWait(context.driver, 10).until(
        # noinspection PyTypeChecker
        EC.url_contains("dashboard"),
        message="Login failed: Dashboard URL did not load within 10 seconds"
    )

    # Once the wait condition passes, we can safely do our final assertion
    assert "dashboard" in context.driver.current_url.lower()