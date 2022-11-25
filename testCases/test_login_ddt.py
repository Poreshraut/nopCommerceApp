import time

from selenium import webdriver
import pytest
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.cutomeLogger import LogGen
from utilities import XLUtilities


class Test_002_DDT_login:
    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()
    path = ".//TestData//DataDrivenTest.xlsx"

    def test_login(self, setup):
        self.logger.info("------------------Test_002_DDT_Login-------------------")
        self.logger.info("------------------Verifying Test Login--------------------")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.ip = LoginPage(self.driver)
        self.rows = XLUtilities.getRowCount(self.path, "DataDrivenTest")
        print('No of rows:', self.rows)
        alist_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtilities.readData(self.path, "DataDrivenTest", r, 1)
            self.passs = XLUtilities.readData(self.path, "DataDrivenTest", r, 2)
            self.exp = XLUtilities.readData(self.path, "DataDrivenTest", r, 3)
            self.ip.setUsername(self.user)
            self.ip.setPassword(self.passs)
            self.ip.clicklogin()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("----------------Passed-----------------")
                    self.ip.clicklogout()
                    alist_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("-------------Failed--------------")
                    self.ip.clicklogout()
                    alist_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("---------------Failed-----------------")
                    alist_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("-------------Passed--------------")
                    alist_status.append("Pass")

        if "Fail" not in alist_status:
            self.logger.info("-------------LoginDDTTest is Passed--------------")
            self.driver.close()
            assert True
        else:
            self.logger.info("--------------LoginDDTTest is Failed----------------")
            self.driver.close()
            assert False

        self.logger.info("----------------End of Login DDT test---------------------")
        self.logger.info("-----------------Completed test cases LoginDDT_002------------------")
