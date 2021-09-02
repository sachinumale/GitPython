import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element_by_css_selector("#confirmbtn").click()
Alert = driver.switch_to.alert
print(Alert.text)
time.sleep(3)
Alert.dismiss()
time.sleep(4)
driver.close()