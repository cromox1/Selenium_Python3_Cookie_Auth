__author__ = 'cromox'

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import remove as removefile
import unittest
import pickle

class TestMengkome1(unittest.TestCase):
    mengkome_url = ''
    cookies = []
    userone = 'bacaone'
    pswdone = 'qawsed123456'

    def setUp(self):
        from platform import system as osname
        if (osname() == 'Windows'):
            chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        elif (osname() == 'Linux'):
            chromedriverpath = '/opt/google/chromedriver/chromedriver'
        else:
            chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(chromedriverpath)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.verificationErrors = []

    def test_one_login(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        driver = self.driver
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        try:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['version']) # Python 3.7 and below
        except:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion']) # Python 3.8 & above
        print()

        user1 = self.__class__.userone
        pswd1 = self.__class__.pswdone
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('username').click()
        driver.find_element_by_name('username').send_keys(user1 + Keys.ENTER)
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys(pswd1 + Keys.ENTER)
        ## write login username/pswd to cookie file
        filename = "cookies.pkl"
        cookiesfile_w = open(filename, "wb")
        pickle.dump(driver.get_cookies(), cookiesfile_w)
        print('GET COOKIES = ' + str(driver.get_cookies()))
        sleep(1)
        cookiesfile_w.close()
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.mengkome_url = driver.current_url
        ## read cookie data and put to cookies variable at the top of the class
        cookiesfile_r = open(filename, "rb")
        self.__class__.cookies = pickle.load(cookiesfile_r)
        cookiesfile_r.close()
        sleep(2)
        ## remove cookie file
        try:
            removefile(filename)
            print('  Successfully remove tmp file ' + filename)
        except WindowsError as exx:
            print('  Error = ' + str(exx) + ' / file = ' + filename)

    def test_two_relogin_chkinfos(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.userone
        urlone = self.__class__.mengkome_url
        driver = self.driver
        driver.get(urlone)
        for cookie in self.__class__.cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
        sleep(1)
        driver.get(urlone)
        userpage1 = driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
        print('Name of the user = ' + userpage1)
        driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
        driver.find_element_by_xpath("//*[contains(text(), '" + user1 + "')]").click()
        email1 = driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
        join1 = driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
        print('User email = ' + email1)
        print('User Joined date = ' + join1)

    def test_x_relogin_then_logout(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        driver = self.driver
        urlone = self.__class__.mengkome_url
        driver.get(urlone)
        for cookie in self.__class__.cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
        sleep(1)
        driver.get(urlone)
        # driver.find_element_by_xpath('//*[@id="user-tools"]/a[3]').click()
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
        if driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
            print('User ' + self.__class__.userone + ' successfully LOGGED OUT')

    def tearDown(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()