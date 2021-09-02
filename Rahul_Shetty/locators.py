from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("Shrikruhsna")
driver.find_element_by_css_selector("[name='email']").send_keys("abc1232@gmail.com")
driver.find_element_by_css_selector("[type='password']").send_keys("1234567890")
driver.find_element_by_css_selector("#exampleCheck1").click()
ele1 = driver.find_elements_by_css_selector("#exampleFormControlSelect1")
for x in ele1:
    print(x.text)
    if x.text == "Male":
        x.click()

# element = Select(driver.find_element_by_css_selector("#exampleFormControlSelect1"))
# element.select_by_visible_text("Male")
driver.find_element_by_css_selector("[type='date']").send_keys(10101990)
driver.find_element_by_css_selector("[type='submit']").click()
msg = driver.find_element_by_css_selector(".alert-success").text

assert msg == "The Form has been submitted successfully!."