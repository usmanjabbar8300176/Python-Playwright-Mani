import re
from playwright.sync_api import sync_playwright, Page, expect


def test_addToCart(page:Page):
    #launch browser
    page.goto("https://automationexercise.com/")
    page.pause()

    #Verify home page
    expect(page).to_have_title(re.compile("Automation Exercise"))

    #Click product button
    page.locator('.material-icons.card_travel').click()

    # Close add popup
    page.get_by_role("button", name="Close ad")

    #AddToCart product1
    page.locator('[data-product-id="1"]').nth(0).click()

    #Click on continue shopping button
    page.locator('.btn.btn-success').click()

    #AddToCart product2
    page.locator('[data-product-id="2"]').nth(0).click()

    #Click on view cart button
    page.locator('.text-center a').nth(0).click()

    #verify product added in cart1
    expect(page.locator('.cart_description').nth(0)).to_contain_text('Blue Top')

    #verify product added in cart2
    expect(page.locator('.cart_description').nth(1)).to_contain_text('Men Tshirt')

    #verify price cart1
    expect(page.locator('.cart_price').nth(0)).to_have_text('Rs. 500')

    #verify price cart2
    expect(page.locator('.cart_price').nth(1)).to_have_text('Rs. 400')

    #verify cart1 quantity
    expect(page.locator('.disabled').nth(0)).to_have_text("1")

     #verify cart2 quantity
    expect(page.locator('.disabled').nth(1)).to_have_text("1")

    #verify cart1 total price
    expect(page.locator('.cart_total_price').nth(0)).to_have_text("Rs. 500")

    #verify cart2 total price
    expect(page.locator('.cart_total_price').nth(1)).to_have_text("Rs. 400")

    #close browser
    page.browser.close()
