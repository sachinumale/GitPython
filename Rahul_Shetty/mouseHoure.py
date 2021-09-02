import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


action = ActionChains(driver)
time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)")
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
time.sleep(3)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform()
driver.get_screenshot_as_file("1.png")
driver.close()