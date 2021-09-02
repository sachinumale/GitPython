import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(5)
element = driver.find_elements(By.XPATH,"//button[text()='ADD TO CART']")

vegList=[]
eVlist=[]
for x in element:
    vegList.append(x.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    x.click()
print(vegList)
driver.find_element(By.CSS_SELECTOR,"[alt='Cart']").click()
#driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")).click().perform()


expVegList = driver.find_elements(By.XPATH,"//p[@class='product-name']")
for x in expVegList:
    eVlist.append(x.text)
print(eVlist)
# assert vegList == expVegList

wait = WebDriverWait(driver,6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element_by_class_name("promoInfo").text)