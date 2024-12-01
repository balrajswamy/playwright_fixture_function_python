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
    page.goto("https://selectorshub.com/xpath-practice-page/",timeout=60000)
    page.wait_for_load_state("networkidle")
    time.sleep(3)  # Reduce unnecessary sleep time
    yield page  # Provide the page object to tests

    # Teardown
    context.close()
    browser.close()
    playwright.stop()  # Ensure Playwright is properly stopped

@pytest.mark.positive
def test_shadow_dom_interating(setup_teardown):
    page = setup_teardown

    element = page.locator('//div[@class="jackPart"]')
    element.scroll_into_view_if_needed()
    time.sleep(3)
    try:
        print("using xpath")
        link_xpath = page.locator("xpath=//div[@class='jackPart']//div[@id='app2']/input[@id='pizza']")
        link_xpath.scroll_into_view_if_needed()
        link_xpath.fill("india pizza using xpath")
    except:
        link_css = page.locator("div.jackPart #app2 #pizza")
        #link.scroll_into_view_if_needed()

        link_css.fill("india pizza using css")
    time.sleep(12)



