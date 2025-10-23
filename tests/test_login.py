import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.login_page import LoginPage
from page.inventory_page import InventoryPage

@pytest.mark.login
def test_login_success(driver):
    login = LoginPage(driver)
    inv = InventoryPage(driver)

    login.open()
    login.login()

    inv.wait_loaded()
    assert "/inventory.html" in driver.current_url
    assert inv.page_title_text() == "Products"
    assert "Swag Labs" in driver.title
