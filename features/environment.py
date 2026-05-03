import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    # This runs right before a Gherkin scenario starts
    print(f"\n--- Starting Scenario: {scenario.name} ---")

    # 1. Setup Chrome Options (The CI/CD Secret)
    chrome_options = Options()

    # ---------------------------------------------------------
    # The Headless Toggle
    # When running on your Mac, keep this commented out to watch it run.
    # When pushing to a CI/CD server, uncomment this so it runs invisibly!

    # ---------------------------------------------------------
    chrome_options.add_argument("--headless=new")
    # ---------------------------------------------------------

    chrome_options.add_argument("--start-maximized") #to see all the visible buttons and page elements

    # 2. Initialize the WebDriver dynamically
    # webdriver-manager automatically downloads the correct driver version
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # 3. Set our Global Implicit Wait (10 seconds) - explain diff between explicit() waits and implicit waits()
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    print(f"--- Finishing Scenario: {scenario.name} ---")

    # THE FIX: Catch absolutely everything that isn't a perfect pass
    if scenario.status.name != 'passed':
        print(f"Scenario failed or broke! Snapping screenshot for: {scenario.name}")

        # 1. Attach the Screenshot
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"Failure_Screenshot_{scenario.name}",
            attachment_type=AttachmentType.PNG
        )

        # 2. Attach the exact URL
        current_url = context.driver.current_url
        allure.attach(
            current_url,
            name="URL_at_time_of_failure",
            attachment_type=AttachmentType.TEXT
        )

    # Safely teardown the browser
    if hasattr(context, 'driver'):
        context.driver.quit()