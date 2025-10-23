#page/inventory_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    URL_FRAGMENT = "/inventory.html"
    TITLE = (By.CLASS_NAME, "title")
    ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def wait_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(self.URL_FRAGMENT)
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        )

    def page_title_text(self):
        return self.driver.find_element(*self.TITLE).text

    def has_products(self):
        return len(self.driver.find_elements(*self.ITEM)) > 0

    def first_item_name_price(self):
        name = self.driver.find_element(*self.ITEM_NAME).text
        price = self.driver.find_element(*self.ITEM_PRICE).text
        return name, price

    def ui_core_elements_present(self):
        self.driver.find_element(*self.MENU_BUTTON)
        self.driver.find_element(*self.SORT_SELECT)
        return True

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
