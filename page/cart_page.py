#page/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    URL_FRAGMENT = "/cart.html"
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_ADD_TO_CART = (By.XPATH, "(//button[contains(@id,'add-to-cart')])[1]")

    def __init__(self, driver):
        self.driver = driver

    def add_first_product_from_inventory(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_ADD_TO_CART)
        ).click()

    def cart_badge_text(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def wait_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(self.URL_FRAGMENT)
        )

    def first_item_name_in_cart(self):
        return self.driver.find_element(*self.CART_ITEM_NAME).text
