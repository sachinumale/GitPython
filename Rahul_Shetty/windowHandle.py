from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#openwindow").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.title)