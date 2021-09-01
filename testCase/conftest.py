import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driversetup():

    driver=webdriver.Chrome(ChromeDriverManager().install())
    return driver