
import re
from playwright.sync_api import sync_playwright, Page, expect

class review_page():
    def __init__(self,page):
        self.page = page

    def visit(self):
        
      #visit the url
      self.page.goto("https://automationexercise.com/")

      # Expect a title "to contain" a substring.
      expect(self.page).to_have_title(re.compile("Automation Exercise"))

      # Click on the "Home" link
      self.page.click('text="Home"')

      # Click on the first panel title
      self.page.locator(".panel-title").nth(1).click()
      # Click on the first element in the nav-justified list
      self.page.locator(".nav-justified ").nth(0).click()

       # Fill in the input field with the value "mani"
      self.page.fill("#name", "mani")

      # Assert that the input field value is "mani"
      expect(self.page.locator("#name")).to_have_value("mani")

      #Fill in the input field with value
      self.page.fill("#email","usmanjabbar+1@gmail.com")

      # Assert that the input field value is "usmanjabbar09@gmail.com"
      expect(self.page.locator("#email")).to_have_value("usmanjabbar+1@gmail.com")

      #Fill in the input field with value
      self.page.fill("#review","Yeah its nice")

      # Assert that the input field value is "mani"
      expect(self.page.locator("#review")).to_have_value("Yeah its nice")

    #Click on submit button
      self.page.locator("#button-review").click()

    
