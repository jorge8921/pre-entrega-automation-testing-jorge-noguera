import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage

@pytest.mark.inventory
def test_inventory_core_elements_and_first_product(driver):
    login = LoginPage(driver)
    inv = InventoryPage(driver)

    login.open()
    login.login()
    inv.wait_loaded()

    assert inv.page_title_text() == "Products"
    assert inv.ui_core_elements_present()
    assert inv.has_products()

    name, price = inv.first_item_name_price()
    print(f"\nPrimer producto: {name} - {price}")
    assert name and price
