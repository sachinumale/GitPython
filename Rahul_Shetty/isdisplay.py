from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

opt = webdriver.ChromeOptions()
opt.add_argument("headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

print(driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed())
driver.find_element(By.ID,"hide-textbox").click()
print(driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed())
driver.close()