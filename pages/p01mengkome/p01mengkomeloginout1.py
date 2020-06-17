__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
# import datetime

class P01LoginLogoutCookie(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ## user/pswd
    user1 = 'bacaone'
    pswd1 = 'qawsed123456'
    # user1 = 'bacatiga'
    # pswd1 = 'lkjhgf098765'
    # Locators login auth (mengkome main page)
    _user_area = 'username'
    _pswd_area = 'password'
    _login_type = 'name'
    # Locators user infos
    _main_type = 'xpath'
    _first_page = '//*[@id="user-tools"]/strong'
    _users_page = "//*[contains(text(), 'Users')]"
    _user_info = str(user1)
    _user_info_type = 'link'
    _email_info = '//*[@class="form-row field-email"]/*/*[@class="readonly"]'
    _join_date = '//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]'
    # Locators logout
    _logout_tb = "//*[contains(text(), 'Log out')]"
    _logout_chk = "//*[@id='content']/h1"

    # Mengkome page
    def keyinUserAuthentication(self):
        self.elementClick(self._user_area, locatorType=self._login_type)
        self.sendKeys(self.user1 + Keys.ENTER, self._user_area, locatorType=self._login_type)
        self.elementClick(self._pswd_area, locatorType=self._login_type)
        self.sendKeys(self.pswd1 + Keys.ENTER, self._pswd_area, locatorType=self._login_type)

    # from First page go to Users page
    def gotoUsersPage(self):
        nameuser = self.getText(self._first_page, locatorType=self._main_type)
        print('Name of the user = ' + nameuser)
        # go to Users page
        self.elementClick(self._users_page, locatorType=self._main_type)
        # go to User to check info
        # self.elementClick(self._user_info, locatorType=self._main_type)
        self.getElementList(self._user_info, locatorType=self._user_info_type)[-1].click()
        emailuser = self.getText(self._email_info, locatorType=self._main_type)
        joindate = self.getText(self._join_date, locatorType=self._main_type)
        print('User email = ' + emailuser)
        print('User Joined date = ' + joindate)
        return nameuser, emailuser, joindate

    # logout (after login)
    def userLogout(self):
        self.elementClick(self._logout_tb, locatorType=self._main_type)
        if self.getText(self._logout_chk, locatorType=self._main_type) == 'Logged out':
            print('User ' + self.user1 + ' successfully LOGGED OUT')

    ## General
    def returnCurrentURL(self):
        return self.driver.current_url

    def gotosite(self, URL):
        return self.driver.get(URL)

    def closeBrowserPage(self):
        return self.driver.close()

    def addcookietosite(self, cookie):
        self.driver.add_cookie(cookie)

    def returnCookies(self):
        print('COOKIES = ' + str(self.driver.get_cookies()))
        return self.driver.get_cookies()

    def returnDomainFrURL(self, url):
        return str(url.split('://')[1].split('/')[0])

    def returnLoginCookie(self, cookies, domainname):
        from time import strftime, localtime
        if len(cookies) >= 1:
            cookie = cookies[0]
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
        else:
            cookie = {'domain': domainname, 'expiry': 0}

        if cookies[0]['domain'] == domainname:
            print('COOKIE [ ' + domainname + ' ] = ' + str(cookie))
        else:
            print('COOKIE [ ' + domainname + ' ] PROBLEM = ' + str(cookie))
        timeexpire = strftime('%Y-%m-%d %H:%M:%S', localtime(cookie['expiry']))
        print('COOKIE EXPIRY = ' + str(timeexpire))
        return cookie