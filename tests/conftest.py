import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    d = get_driver()
    yield d
    d.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver")
        if drv:
            folder = os.path.join("reports", "screenshots")
            os.makedirs(folder, exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"{item.nodeid.replace('::','_')}_{ts}.png".replace('/', '_')
            path = os.path.join(folder, name)
            drv.save_screenshot(path)
            print(f"\nScreenshot guardada: {path}")
