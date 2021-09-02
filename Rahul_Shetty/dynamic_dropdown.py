from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver =  webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://paytm.com/bus-tickets")
driver.find_element_by_css_selector("[class='fl-input']").send_keys("pu")
city = driver.find_elements_by_xpath("//div[@class='_2xgL']/div/p[2]")

for x in city:
    print(x.text)