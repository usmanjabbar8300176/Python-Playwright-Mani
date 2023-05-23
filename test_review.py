
import re
from playwright.sync_api import sync_playwright, Page, expect

def test_review(page: Page):
    #visit the url
    page.goto("https://automationexercise.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on the "Home" link
    page.click('text="Home"')

    # Click on the first panel title
    page.locator(".panel-title").nth(1).click()
    # Click on the first element in the nav-justified list
    page.locator(".nav-justified ").nth(0).click()

     # Fill in the input field with the value "mani"
    page.fill("#name", "mani")

    # Assert that the input field value is "mani"
    expect(page.locator("#name")).to_have_value("mani")

    #Fill in the input field with value
    page.fill("#email","usmanjabbar+1@gmail.com")

    # Assert that the input field value is "usmanjabbar09@gmail.com"
    expect(page.locator("#email")).to_have_value("usmanjabbar+1@gmail.com")

    #Fill in the input field with value
    page.fill("#review","Yeah its nice")

      # Assert that the input field value is "mani"
    expect(page.locator("#review")).to_have_value("Yeah its nice")

    #Click on submit button
    page.locator("#button-review").click()

    #close browser
    page.browser.close()
