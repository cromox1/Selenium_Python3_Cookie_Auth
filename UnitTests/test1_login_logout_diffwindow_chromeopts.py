__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import strftime, localtime
import unittest

class TestMengkome1(unittest.TestCase):
    mengkome_url = ''
    user1 = ''
    cookie = {}
    cookies = []
    ixi = 0

    def setUp(self):
        from platform import system as osname
        if (osname() == 'Windows'):
            self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        elif (osname() == 'Linux'):
            self.chromedriverpath = '/opt/google/chromedriver/chromedriver'
        else:
            self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.chrome_options = Options()
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--allow-running-insecure-content")
        self.chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        self.chrome_options.add_argument("--disable-cookie-encryption")
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument("--test-type")
        ## webdriver section
        self.driver = webdriver.Chrome(self.chromedriverpath, options=self.chrome_options)
        print('\n--- >> SETUP')
        self.__class__.ixi = self.__class__.ixi + 1

    def test_01_login(self):
        print('\n' + str(self.__class__.ixi) + ') ---->  ' + str(self._testMethodName) + '\n')
        ## user/pswd
        # user1 = 'bacaone'
        # pswd1 = 'qawsed123456'
        user1 = 'bacatiga'
        pswd1 = 'lkjhgf098765'
        ## GET python version & Browser version
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        from selenium import __version__ as seleniumversion
        print('Selenium version = ' + seleniumversion)

        try:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['version']) # Python 3.7 and below
        except:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion']) # Python 3.8 & above
        print()

        print("CHROME_OPTIONS = " + str(self.chrome_options.arguments))
        self.driver.implicitly_wait(10)

        if self.driver.name == 'chrome':
            self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.find_element_by_name('username').click()
        self.driver.find_element_by_name('username').send_keys(user1 + Keys.ENTER)
        self.driver.find_element_by_name('password').click()
        self.driver.find_element_by_name('password').send_keys(pswd1 + Keys.ENTER)

        self.__class__.mengkome_url = self.driver.current_url
        self.__class__.user1 = user1
        self.__class__.cookies = self.driver.get_cookies()

    def test_02_relogin_chkinfos(self):
        print('\n' + str(self.__class__.ixi) + ') ---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.user1
        urlone = self.__class__.mengkome_url

        self.driver.get(urlone)
        print('CURRENT URL = ' + self.driver.current_url)
        # # cookies
        urlx = str(urlone.split('://')[1].split('/')[0])
        cookies = self.__class__.cookies
        if len(cookies) >= 1:
            self.__class__.cookie = cookies[0]
            if 'expiry' in self.__class__.cookie:
                self.__class__.cookie['expiry'] = int(self.__class__.cookie['expiry'])
        else:
            self.__class__.cookie = {'domain': urlx, 'expiry': 0}

        if cookies[0]['domain'] == urlx:
            print('COOKIE [ ' + urlx + ' ] = ' + str(self.__class__.cookie))
        else:
            print('COOKIE [ ' + urlx + ' ] PROBLEM = ' + str(self.__class__.cookie))
        timeexpire = strftime('%Y-%m-%d %H:%M:%S', localtime(self.__class__.cookie['expiry']))
        print('COOKIE EXPIRY = ' + str(timeexpire))
        self.driver.add_cookie(self.__class__.cookie)

        self.driver.get(urlone)
        userpage1 = self.driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
        print('Name of the user = ' + userpage1)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
        print('CHECK USER1 = ' + str(user1))
        # self.driver.find_element_by_xpath("//*[contains(text(), '" + str(user1) + "')]").click()
        self.driver.find_elements_by_link_text(str(user1))[-1].click() # user has grp with the same name
        email1 = self.driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
        join1 = self.driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
        print('User email = ' + email1)
        print('User Joined date = ' + join1)
        self.__class__.mengkome_url = self.driver.current_url

    def test_90_relogin_then_logout(self):
        print('\n' + str(self.__class__.ixi) + ') ---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.user1
        urlone = self.__class__.mengkome_url

        self.driver.get(urlone)
        print('CURRENT URL = ' + self.driver.current_url)
        self.driver.add_cookie(self.__class__.cookie)
        self.driver.get(urlone)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
        if self.driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
            print('User ' + user1 + ' successfully LOGGED OUT')

    def test_99_cookie_notuseable(self):
        print('\n' + str(self.__class__.ixi) + ') ---->  ' + str(self._testMethodName) + '\n')
        urlone = self.__class__.mengkome_url
        user1 = self.__class__.user1

        self.driver.get(urlone)
        print('CURRENT URL = ' + self.driver.current_url)
        self.driver.add_cookie(self.__class__.cookie)
        self.driver.get(urlone)
        pagetitle = self.driver.title
        print('TITLE = ' + str(pagetitle))
        # not login anymore -- > Cookie is not usable
        if 'Log in' in pagetitle:
            print('User ' + user1 + ' is OUTSIDE the page - Cookie is UNUSABLE')
        else:
            print('User ' + user1 + ' look like inside - Cookie is USABLE')

    def tearDown(self):
        ## current URL before quit/exit
        print('CURRENT URL = ' + self.driver.current_url)
        # self.driver.close()
        self.driver.quit()
        print('\n--- >> TEARDOWN')
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()