# from playwright.sync_api import sync_playwright

# def automate_website():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch()
#         page = browser.new_page()
#         page.goto("https://automationexercise.com/")

#         # Fill in the form
#         # page.fill('input[name="FirstName"]', 'John')
#         # page.fill('input[name="LastName"]', 'Doe')
#         # page.fill('input[name="EmailAdress"]', 'johndoe@example.com')
#         # page.fill('input[name="Phone"]', '1234567890')
#         # page.fill('input[name="CompanyName"]', 'Example Inc.')

#         # # Submit the form
#         # page.click('input[type="submit"]')

#         # # Wait for the success message to appear
#         # page.wait_for_selector('div[id="message"]')

#         # # Get the success message text
#         # success_message = page.inner_text('div[id="message"]')
#         # print(success_message)

#         browser.close()

# automate_website()


# import re
# from playwright.sync_api import Page, expect


# def test_automation_website(page: Page):
#     page.goto("https://automationexercise.com/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Automation Exercise"))
#     page.click('text="Home"')  
#     page.locator(".panel-title").locator("nth=1").click()
#     page.locator(".nav-justified").locator("nth=0").click()
#     page.fill("#name", "mani")
#     expect(page.locator("#name")).to_have_value("mani")

import re
from playwright.sync_api import sync_playwright, Page, expect


def test_automation_website(page: Page):
    page.goto("https://automationexercise.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on the "Home" link
    page.click('text="Home"')

    # Click on the first panel title
    page.locator(".panel-title").nth(1).click()

    # Click on the first element in the nav-justified list
    page.locator(".nav-justified ").nth(0).click()

    # # Fill in the input field with the value "mani"
    # page.fill("#name", "mani")

    # # Assert that the input field value is "mani"
    # expect(page.locator("#name")).to_have_value("mani")


