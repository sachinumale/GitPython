from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoWebLogin:
    login_link_xpath = "//a[text()='Log in']"
    email_textbox_cssClass =".email"
    password_textbox_cssID = "#Password"
    login_button_cssValue ="input[value='Log in']"

    def __init__(self,driver):
        self.driver = driver

    def clickLinkButton(self):
        self.driver.find_element(By.XPATH,self.login_link_xpath).click()

    def setUserName(self,username):
        self.driver.find_element(By.CSS_SELECTOR, self.email_textbox_cssClass).clear()
        self.driver.find_element(By.CSS_SELECTOR,self.email_textbox_cssClass).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.CSS_SELECTOR,self.password_textbox_cssID).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.password_textbox_cssID).send_keys(password)

    def submitButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_cssValue).click()
