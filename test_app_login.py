import pytest
import allure
from playwright.sync_api import sync_playwright, Page,expect
import time


@pytest.fixture(scope="function")
def setup_teardown():
    """Fixture to initialize and teardown Playwright browser and page."""
    playwright = sync_playwright().start()  # Start Playwright
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(60000)

    # Load the login page
    page.goto("https://app.vwo.com",timeout=60000)
    page.wait_for_load_state("networkidle")
    time.sleep(3)  # Reduce unnecessary sleep time
    yield page  # Provide the page object to tests

    # Teardown
    context.close()
    browser.close()
    playwright.stop()  # Ensure Playwright is properly stopped

@pytest.mark.negative
def test_vwo_Login_negative(setup_teardown):
    #initializing the browser and page
    page = setup_teardown

    #locate the web elements
    page.locator('//input[@id="login-username"]').click()
    page.locator('//input[@id="login-username"]').clear()
    page.locator('//input[@id="login-username"]').fill("admin@gmail.com")
    page.wait_for_timeout(100)
    page.locator('//input[@id="login-password"]').click()
    page.locator('//input[@id="login-password"]').click()
    page.locator('//input[@id="login-password"]').fill("admin123")
    page.wait_for_timeout(100)
    page.locator('//button[@id="js-login-btn"]').click()
    time.sleep(3)
    error_msg_selector = '//div[@id="js-notification-box-msg"]'
    page.wait_for_selector(error_msg_selector)
    error_message = page.locator(error_msg_selector)
    assert error_message.text_content() == 'Your email, password, IP address or location did not match'

@pytest.mark.positive
def test_vwo_Login_positive(setup_teardown):
    page = setup_teardown

    #locate the web elements
    page.locator('//input[@id="login-username"]').click()
    page.locator('//input[@id="login-username"]').clear()
    page.locator('//input[@id="login-username"]').fill("admin@gmail.com")
    page.wait_for_timeout(100)
    page.locator('//input[@id="login-password"]').click()
    page.locator('//input[@id="login-password"]').click()
    page.locator('//input[@id="login-password"]').fill("admin123")
    page.wait_for_timeout(100)
    page.locator('//button[@id="js-login-btn"]').click()
    time.sleep(3)
    error_msg_selector = '//div[@id="js-notification-box-msg"]'
    page.wait_for_selector(error_msg_selector)
    error_message = page.locator(error_msg_selector)
    assert error_message.text_content() == 'Your email, password, IP address or location did not match'


