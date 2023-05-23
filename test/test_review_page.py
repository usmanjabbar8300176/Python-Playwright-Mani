import pytest
from playwright.sync_api import sync_playwright
from pages.review_page_po.review_page import review_page

@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    
def test_review_page(browser):
    page = browser.new_page()
    reviewPage = review_page(page)
    reviewPage.visit()
