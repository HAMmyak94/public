import pytest


@pytest.fixture
def driver(driver):
    driver.binary = "C:/driver.exe"
    return driver