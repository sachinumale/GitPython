import unittest
import html_test_report
from selenium import webdriver
from DemoWebShop1.pageObject.LoginPage import DemoWebLogin
from webdriver_manager.chrome import ChromeDriverManager

# import sys
# sys.path.append("C:/Users/ina260shrkhed/PycharmProjects/TricentisDemoWebshop")


class LoginTest(unittest.TestCase):
    baseURL = "http://demowebshop.tricentis.com/"
    emailUsername = "8856867072"
    password = "1234567890"
    driver  = webdriver.Chrome(ChromeDriverManager().install())


    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = DemoWebLogin(self.driver)
        lp.clickLinkButton()
        lp.setUserName(self.emailUsername)
        lp.setPassword(self.password)
        lp.submitButton()
        print("Title of home page is: ",self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__()":
    unittest.main(testRunner=html_test_report.HtmlTestRunner("C:/Users/ina260shrkhed/PycharmProjects/TricentisDemoWebshop/DemoWebShop1/reports"))