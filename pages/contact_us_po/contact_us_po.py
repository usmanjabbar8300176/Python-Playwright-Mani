import re
from playwright.sync_api import expect

class contact_us_page:
    def __init__(self,page):
        self.page = page

    def visit(self):
      self.page.pause() 
      # Visit the URL
      self.page.goto("https://automationexercise.com/")
 
      # Click on the contactUs button
      self.page.locator(".fa.fa-envelope").click()

      # Verify text on another page
      expect(self.page.locator('.title.text-center').nth(1)).to_have_text(re.compile(r"Get In Touch"))

       # Enter Name
      self.page.locator('.form-control').nth(0).fill("usman")

      # Enter Email
      self.page.locator('.form-control').nth(1).fill("usman@gmail.com")

      # Enter Subject
      self.page.locator('.form-control').nth(2).fill('Testing')

      # Enter message
      self.page.locator('.form-control').nth(3).fill('I am using this site for testing purpose')

      # Click on submit button
      self.page.locator('[value="Submit"]').click()

      #Click on ok button
      self.page.on("dialog", handle_alert)

    
def handle_alert(page):
    def dialog_handler(dialog):
        dialog.accept()
    page.on("dialog", dialog_handler)
    page.browser.close()


