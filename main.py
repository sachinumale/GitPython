# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#--------------------------------------------------

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# option = webdriver.ChromeOptions()
# option.add_argument("headless")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demowebshop.tricentis.com/")
driver.implicitly_wait(5)
driver.maximize_window()
ti1 = driver.title
print(ti1)
print(driver.current_url)
driver.find_element_by_class_name("ico-login").click()
driver.find_element(By.ID,"Email" ).send_keys("abc@gmail.com")
driver.find_element(By.NAME,"Password").send_keys("123456789")
driver.find_element(By.XPATH,"//*[@type='submit'][@value='Log in']").click()
Actual = "Login was unsuccessful. Please correct the errors and try again."
Expected=driver.find_element(By.XPATH,"//*[text()='Login was unsuccessful. Please correct the errors and try again.']").text
print("Actual:",Actual)
print("Expected:",Expected)
assert Actual==Expected
driver.find_element(By.XPATH,"//input[@class='button-1 register-button']").click()
driver.find_element(By.CSS_SELECTOR,"#gender-male").click()
driver.find_element(By.CSS_SELECTOR,"#FirstName").send_keys("Shrikrushna")
driver.find_element(By.CSS_SELECTOR,"#LastName").send_keys("Khedkar")
driver.find_element(By.XPATH,"//div[@class='form-fields']/div[4]/input").send_keys("885686@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#Password").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR,"#ConfirmPassword").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR,".register-next-step-button").click()
driver.find_element(By.CSS_SELECTOR,"[type='button']").click()
actual = driver.find_element(By.XPATH,"//div[@class='validation-summary-errors']/ul/li").text
expected = "The specified email already exists"

assert actual==expected
driver.find_element_by_link_text("Log in").click()
driver.find_element(By.CSS_SELECTOR,"[id*='Email']").send_keys("885686@gmail.com")
driver.find_element(By.CSS_SELECTOR,".password").send_keys("123456789")
driver.find_element(By.XPATH,"//input[@value='Log in']").click()

action = ActionChains(driver)
#ele1 = driver.find_elements(By.CSS_SELECTOR,"//ul[@class='top-menu']/li[2]/a")
action.move_to_element(driver.find_element(By.XPATH,"//ul[@class='top-menu']/li[2]/a")).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.XPATH,"//ul[@class='top-menu']/li[2]/ul/li[1]")).click().perform()

coumputerItem = driver.find_elements(By.XPATH,"//div[@class='product-item']/div/h2/a")

#//div[@class='product-item']/div[2]/div/div[2]/input
for computer in coumputerItem:
    product = computer.text
    print(product)
    addToCart = driver.find_elements(By.XPATH,"//div[@class='product-item']/div[2]/div/div[2]/input")

    for addToCarts in addToCart:
        if product == 'Build your own expensive computer':
            addToCarts.click()

# driver.find_element(By.CSS_SELECTOR,"#addtocart_74_EnteredQuantity").clear()
# driver.find_element(By.CSS_SELECTOR,"#addtocart_74_EnteredQuantity").send_keys(12)
# time.sleep(4)
# ele = driver.find_element(By.XPATH,"//div[@class='add-to-cart']/div[1]/input[2]")
# driver.execute_script("arguments[0].click();",ele)
# sucessMsg = driver.find_element(By.CSS_SELECTOR,"[class='bar-notification success'] p").text
# print(sucessMsg)
