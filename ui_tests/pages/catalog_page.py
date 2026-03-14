class CatalogPage:
    def __init__(self, page):
        self.page = page
        self.products = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def get_product_count(self):
        return self.products.count()

    def add_first_product_to_cart(self):
        self.products.first.locator("button").click()

    def get_cart_count(self):
        return self.cart_badge.text_content()

    def go_to_cart(self):
        self.cart_link.click()
