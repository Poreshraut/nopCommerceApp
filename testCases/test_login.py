import time

from selenium import webdriver
import pytest
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.cutomeLogger import LogGen


class Test_001_login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_Homepage(self, setup):
        self.logger.info("---------------------Test_001_Login----------------------")
        self.logger.info("--------------------Verifying the HomePage Title---------------------")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("--------------------HomePage Title Test Is Passed---------------------")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.logger.info("-------------------HomePage Title Test Is Failed----------------------")
            assert False

    def test_login(self, setup):
        self.logger.info("------------------Verifying Test Login--------------------")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.ip = LoginPage(self.driver)
        self.ip.setUsername(self.username)
        self.ip.setPassword(self.password)
        self.ip.clicklogin()
        act_title = self.driver.title
        time.sleep(5)

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("-----------------Test Login Is Passed-------------------")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.info("---------------Test Login Is Failed------------------")
            assert False

