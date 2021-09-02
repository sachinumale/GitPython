import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import readConfig
from pageObject.LoginScreen import Login
from utilities.customeLogger import loGen
class Test_001_Login:
    webUrl= readConfig.getApplicationUrl()
    username= readConfig.getusername()
    password=readConfig.getPassword()
    logger=loGen.loggen()

    def test_homeTitle(self,driversetup):
        self.logger.info("**************Test__001_Login****************")
        self.logger.info("**************Verifying Title****************")
        self.driver=driversetup
        self.driver.get(self.webUrl)
        actual=self.driver.title

        print(actual)
        if actual=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Title Passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homeTitle.png")
            self.driver.close()

            self.logger.error("**************Title Failed*****************")
            assert False


    def test_Login(self,driversetup):
        self.logger.info("**************Verifying Login Test****************")
        self.driver = driversetup
        self.driver.get(self.webUrl)
        self.obj=Login(self.driver)
        self.obj.setUserName(self.username)
        self.obj.setPassword(self.password)
        self.obj.logIn()
        actual=self.driver.title

        print(actual)
        if actual=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************Login Test Passed*****************")
            self.driver.close()
        else:
            self.driver.save_screenshot

            self.logger.error("**************Login Test Failed*****************")
            self.driver.close()
            assert False




