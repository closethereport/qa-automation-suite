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

    def sort_by(self, option: str):
        self.page.locator(".product_sort_container").select_option(option)

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def get_product_prices(self):
        texts = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(p.replace("$", "")) for p in texts]
