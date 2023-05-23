#import re
import pytest
from playwright.sync_api import sync_playwright
from pages.contact_us_po.contact_us_po import contact_us_page

@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    
def test_contact_Us(browser):
    page = browser.new_page()
    contactPage = contact_us_page(page)
    contactPage.visit()
