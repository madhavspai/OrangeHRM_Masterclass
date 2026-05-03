import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    print(f"\n--- Starting Scenario: {scenario.name} ---")

    chrome_options = Options()

    # ESSENTIAL FOR CI/CD STABILITY
    # ---------------------------------------------------------
    chrome_options.add_argument("--headless=new") # Run invisibly
    chrome_options.add_argument("--no-sandbox") # Required for Linux environments
    chrome_options.add_argument("--disable-dev-shm-usage") # Prevents memory-related crashes
    chrome_options.add_argument("--window-size=1920,1080") # Ensures elements are within view
    # ---------------------------------------------------------

    chrome_options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Note: Implicit wait is removed to allow Explicit Waits in Page Objects
    # to handle synchronization reliably without interference.

def after_scenario(context, scenario):
    print(f"--- Finishing Scenario: {scenario.name} ---")

    if scenario.status.name != 'passed':
        print(f"Scenario failed! Snapping screenshot for: {scenario.name}")

        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"Failure_Screenshot_{scenario.name}",
            attachment_type=AttachmentType.PNG
        )

        allure.attach(
            context.driver.current_url,
            name="URL_at_time_of_failure",
            attachment_type=AttachmentType.TEXT
        )

    if hasattr(context, 'driver'):
        context.driver.quit()