from playwright.sync_api import expect

class add_to_cart:
    def __init__(self, page):
        self.page = page

    def visit(self):
        #launch browser
        self.page.goto("https://automationexercise.com/")
        self.page.pause()
    def add_item(self):
        #click product button
        self.page.locator('.material-icons.card_travel').click()        
        # Close add popup
        self.page.get_by_role("button", name="Close ad")
        #AddToCart product1
        self.page.locator('[data-product-id="1"]').nth(0).click()
        #Click on continue shopping button
        self.page.locator('.btn.btn-success').click()
        #AddToCart product2
        self.page.locator('[data-product-id="2"]').nth(0).click()


    def view_cart(self):
        #Click on view cart button
        self.page.locator('.text-center a').nth(0).click()
    
    def verify_cart(self):
        #verify product added in cart1
        expect(self.page.locator('.cart_description').nth(0)).to_contain_text('Blue Top')

        # verify product added in cart2
        expect(self.page.locator('.cart_description').nth(1)).to_contain_text('Men Tshirt')

        # verify price cart1
        expect(self.page.locator('.cart_price').nth(0)).to_have_text('Rs. 500')

        # verify price cart2
        expect(self.page.locator('.cart_price').nth(1)).to_have_text('Rs. 400')

        # verify cart1 quantity
        expect(self.page.locator('.disabled').nth(0)).to_have_text("1")

        # verify cart2 quantity
        expect(self.page.locator('.disabled').nth(1)).to_have_text("1")

        # verify cart1 total price
        expect(self.page.locator('.cart_total_price').nth(0)).to_have_text("Rs. 500")

        # verify cart2 total price
        expect(self.page.locator('.cart_total_price').nth(1)).to_have_text("Rs. 400")
