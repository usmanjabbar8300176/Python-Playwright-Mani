import pytest
import re
from playwright.sync_api import sync_playwright
from pages.add_to_cartPO.add_to_cart_po import add_to_cart

@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

def test_cart(browser):
    page = browser.new_page()
    cart_items = add_to_cart(page)
    cart_items.visit()
    assert re.search("Automation Exercise", page.title())
    cart_items.add_item()
    cart_items.view_cart()
    cart_items.verify_cart()