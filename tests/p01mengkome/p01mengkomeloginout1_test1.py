__author__ = 'cromox'

from pages.p01mengkome.p01mengkomeloginout1 import P01LoginLogoutCookie
from utilities.teststatus import TestStatus as tStatus
from time import strptime, mktime
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import sys

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class P01MengkomeLoginLogoutTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    urlnow = ''
    cookie = {}
    ix = 0

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.mengkomepage = P01LoginLogoutCookie(self.driver)
        self.tstatus = tStatus(self.driver)
        print('\n--- >> SETUP')
        self.__class__.ix = self.__class__.ix + 1

    # @pytest.mark.run(order=1)
    # @pytest.mark.tryfirst
    def test1_login_mengkome_add_cookie_page(self):
        mengkome_url = 'https://mengkome.pythonanywhere.com'
        print('\n' + str(self.__class__.ix) + ') -- >  ' + str(self._testMethodName) + '\n')
        # login with user/pswd auth & add cookie
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        self.mengkomepage.gotosite(mengkome_url)
        result = self.mengkomepage.verifyPageURLlow(mengkome_url)
        self.tstatus.mark(result, "Currently At Mengkome Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.verifyWordExistInURL('mengkome')
        self.tstatus.mark(result, "mengkome word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.mengkomepage.keyinUserAuthentication()
        self.cookies = self.mengkomepage.returnCookies()
        result = self.mengkomepage.verifyActualGreaterEqualExpected(len(self.cookies), 1)
        self.tstatus.mark(result, "Cookies list Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        domainmengkome = self.mengkomepage.returnDomainFrURL(mengkome_url)
        self.__class__.cookie = self.mengkomepage.returnLoginCookie(self.cookies, domainmengkome)
        result = self.mengkomepage.verifyDateIsFuture(self.__class__.cookie['expiry'])
        self.tstatus.mark(result, "Cookie expiry date Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.verifyTextEqual(self.__class__.cookie['domain'], domainmengkome)
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("Login & cookie Verified", result, sys._getframe().f_code.co_name)
        self.__class__.urlnow = self.mengkomepage.returnCurrentURL()

    # @pytest.mark.run(order=2)
    # @pytest.mark.trylast
    def test2_relogin_bycookie_chkinfos(self):
        print('\n' + str(self.__class__.ix) + ') -- >  ' + str(self._testMethodName) + '\n')
        # auto login using test1 cookie & chk infos
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        urlcurrent = self.__class__.urlnow
        print('MENGKOME_URL = ' + urlcurrent)
        self.mengkomepage.gotosite(urlcurrent)
        result = self.mengkomepage.verifyPageURLlow('https://mengkome.pythonanywhere.com')
        self.tstatus.mark(result, "Currently At Mengkome Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.mengkomepage.addcookietosite(self.__class__.cookie)
        self.mengkomepage.gotosite(urlcurrent)
        print('URL = ' + str(self.mengkomepage.returnCurrentURL()))
        userinfos = self.mengkomepage.gotoUsersPage()
        result = self.mengkomepage.verifyActualGreaterEqualExpected(len(userinfos[0]), 1)
        self.tstatus.mark(result, "Username " + userinfos[0] + ' existance Verified')
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.verifyEmailFormat(userinfos[1])
        self.tstatus.mark(result, "Email (format) Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        # date joined format = 'Nov. 8, 2018, 2:08 p.m.'
        textdate = userinfos[2].replace(',', '').replace('p.m.', 'pm').replace('a.m.', 'am')
        joineddate = " ".join(textdate.split(" ")[:])
        try:
            joinedepoch = mktime(strptime(joineddate, "%b. %d %Y %I:%M %p"))
        except:
            joinedepoch = mktime(strptime(joineddate, "%B %d %Y %I:%M %p"))
        result = self.mengkomepage.verifyDateIsHistory(joinedepoch)
        self.tstatus.mark(result, "Date joined Verified")
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("Relogin by cookie & chk infos Verified", result, sys._getframe().f_code.co_name)
        self.__class__.urlnow = self.mengkomepage.returnCurrentURL()

    def test3_relogin_bycookie_logout(self):
        print('\n' + str(self.__class__.ix) + ') -- >  ' + str(self._testMethodName) + '\n')
        # auto relogin then logout
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        urlcurrent = self.__class__.urlnow
        print('Current URL = ' + urlcurrent)
        self.mengkomepage.gotosite(urlcurrent)
        result = self.mengkomepage.verifyPageURLlow('https://mengkome.pythonanywhere.com')
        self.tstatus.mark(result, "Currently At Mengkome Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.mengkomepage.addcookietosite(self.__class__.cookie)
        self.mengkomepage.gotosite(urlcurrent)
        result = self.mengkomepage.verifyPageTitle("View user | Django site admin")
        self.tstatus.mark(result, "User page title Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.isElementPresent("//*[contains(text(), 'View site')]", locatorType='xpath')
        self.tstatus.mark(result, "Inside Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.mengkomepage.userLogout()
        result = self.mengkomepage.verifyPageTitle("Logged out | Django site admin")
        self.tstatus.mark(result, "Logged out page title Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.isElementPresent("//*[contains(text(), 'Logged out')]", locatorType='xpath')
        self.tstatus.mark(result, "Logged out element Verified")
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("Relogin by cookie & then Log-out Verified", result, sys._getframe().f_code.co_name)

    def test9_relogin_after_logout(self):
        print('\n' + str(self.__class__.ix) + ') -- >  ' + str(self._testMethodName) + '\n')
        # auto relogin after logout
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        urlcurrent = self.__class__.urlnow
        print('Current URL = ' + urlcurrent)
        self.mengkomepage.gotosite(urlcurrent)
        self.mengkomepage.addcookietosite(self.__class__.cookie)
        self.mengkomepage.gotosite(urlcurrent)
        result = self.mengkomepage.verifyPageTitle("Log in | Django site admin")
        self.tstatus.mark(result, "Front page / Login title Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        # '//*[@id="login-form"]'
        result = self.mengkomepage.isElementPresent("login-form", locatorType='id')
        self.tstatus.mark(result, "Login element Verified")
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("Relogin by cookie not allowed Verified", result, sys._getframe().f_code.co_name)

    def tearDown(self):
        print('CURRENT URL = ' + str(self.mengkomepage.returnCurrentURL()))
        print('\n--- >> TEARDOWN')
        # self.mengkomepage.driver.close()