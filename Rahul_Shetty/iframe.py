from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
driver.switch_to.frame("courses-iframe")
print(driver.title)
driver.switch_to.default_content()
print(driver.title)
