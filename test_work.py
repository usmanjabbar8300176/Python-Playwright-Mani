

import re
from playwright.sync_api import sync_playwright, Page, expect

# def test_automation_website(page: Page):
#     #visit the url
#     page.goto("https://automationexercise.com/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Automation Exercise"))

#     # Click on the "Home" link
#     page.click('text="Home"')

#     # Click on the first panel title
#     page.locator(".panel-title").nth(1).click()
#     # Click on the first element in the nav-justified list
#     page.locator(".nav-justified ").nth(0).click()

#      # Fill in the input field with the value "mani"
#     page.fill("#name", "mani")

#     # Assert that the input field value is "mani"
#     expect(page.locator("#name")).to_have_value("mani")

#     #Fill in the input field with value
#     page.fill("#email","usmanjabbar+1@gmail.com")

#     # Assert that the input field value is "usmanjabbar09@gmail.com"
#     expect(page.locator("#email")).to_have_value("usmanjabbar+1@gmail.com")

#     #Fill in the input field with value
#     page.fill("#review","Yeah its nice")

#       # Assert that the input field value is "mani"
#     expect(page.locator("#review")).to_have_value("Yeah its nice")

#     #Click on submit button
#     page.locator("#button-review").click()
#     page.pause()

#     #close browser
#     page.browser.close()

 
def test_contactUs_page(page: Page):
    # Visit the URL
    page.goto("https://automationexercise.com/")
 
    # Click on the contactUs button
    page.locator(".fa.fa-envelope").click()

    # Verify text on another page
    expect(page.locator('.title.text-center').nth(1)).to_have_text(re.compile(r"Get In Touch"))

    # Enter Name
    page.locator('.form-control').nth(0).fill("usman")

    # Enter Email
    page.locator('.form-control').nth(1).fill("usman@gmail.com")

    # Enter Subject
    page.locator('.form-control').nth(2).fill('Testing')

    # Enter message
    page.locator('.form-control').nth(3).fill('I am using this site for testing purpose')

    # Click on submit button
    page.locator('[value="Submit"]').click()


    #Click on ok button
    page.on("dialog", handle_alert)

    
def handle_alert(page):
    def dialog_handler(dialog):
        dialog.accept()
    page.on("dialog", dialog_handler)
    page.browser.close()

