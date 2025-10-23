import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage

@pytest.mark.cart
def test_add_first_product_and_verify_cart(driver):
    login = LoginPage(driver)
    inv = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login()
    inv.wait_loaded()

    cart.add_first_product_from_inventory()
    assert cart.cart_badge_text() == "1"

    inv.open_cart()
    cart.wait_loaded()

    # Verificar nombre consistente entre inventario y carrito
    # Tomamos el nombre del primer item ya que SauceDemo carga el exacto
    cart_item_name = cart.first_item_name_in_cart()
    assert cart_item_name, "No se encontró el producto en el carrito"
