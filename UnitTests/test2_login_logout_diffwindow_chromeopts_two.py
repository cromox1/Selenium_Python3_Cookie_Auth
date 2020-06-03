__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import rmtree as removedir
from time import sleep
import unittest
import browser_cookie3

class TestMengkome1(unittest.TestCase):
    mengkome_url = ''
    chromedatadir = 'chromedata'
    userone = 'bacaone'
    pswdone = 'qawsed123456'
    cookie = {}
    cookies = []

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print('TEST INIT')

    def setUp(self):
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        # self.driver = webdriver.Chrome(self.chromedriverpath)
        print('\n--- >> SETUP')

    def test_01_login(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        from selenium import __version__ as seleniumversion
        print('Selenium version = ' + seleniumversion)

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")ASD
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--test-type")
        ## new one ####
        experimentalFlags = ['same-site-by-default-cookies@1', 'cookies-without-same-site-must-be-secure@1']
        chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
        chrome_options.add_experimental_option('localState', chromeLocalStatePrefs)
        chrome_options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                         'profile': {'password_manager_enabled': False}})
        ## webdriver section
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)
        try:
            print('Browser version ( ' + driver.name + ' ) = ' + driver.capabilities['version']) # Python 3.7 and below
        except:
            print('Browser version ( ' + driver.name + ' ) = ' + driver.capabilities['browserVersion']) # Python 3.8 & above
        print()

        print("CHROME_OPTIONS = " + str(chrome_options.arguments))
        driver.implicitly_wait(10)

        user1 = self.__class__.userone
        pswd1 = self.__class__.pswdone
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('username').click()
        driver.find_element_by_name('username').send_keys(user1 + Keys.ENTER)
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys(pswd1 + Keys.ENTER)

        ## current URL
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.mengkome_url = driver.current_url
        # print(driver.get_cookies())
        self.__class__.cookies = driver.get_cookies()
        driver.close()
        # driver.quit()

    def test_02_relogin_chkinfos(self):
        # import browser_cookie3
        # sleep(2)
        print('\n---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.userone
        urlone = self.__class__.mengkome_url

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-web-security")
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        chrome_options.add_argument("--disable-cookie-encryption")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--test-type")
        ## new one ####
        # experimentalFlags = ['same-site-by-default-cookies@1', 'cookies-without-same-site-must-be-secure@1']
        # chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
        # chrome_options.add_experimental_option('localState', chromeLocalStatePrefs)
        chrome_options.add_experimental_option('prefs', {'credentials_enable_service': True,
                                                         'profile': {'password_manager_enabled': True}})
        ## webdriver section
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)
        # urlonetwo = urlone.split('//')[0]+'//'+self.__class__.userone+':'+self.__class__.pswdone+'@'+urlone.split('//')[1]
        # print(urlonetwo)
        # driver.get(urlonetwo)
        driver.get(urlone)
        # # cookies
        urlx = str(urlone.split('://')[1].split('/')[0])
        # cookies = browser_cookie3.chrome(domain_name=urlx, cookie_file=str(self.__class__.chromedatadir)+'\\Default\\Cookies')
        # cookies = browser_cookie3.chrome(domain_name=
        cookies = self.__class__.cookies
        # print('COOKIES_ALL = ' + str(cookies))
        # print('COOKIE_ALL [ ' + urlx + ' ] = ' + str(cookies))
        if len(cookies) >= 1:
            self.__class__.cookie = cookies[0]
            # cookie = {}
        #     for c in cookies:
        #         self.__class__.cookie = {'domain': c.domain,
        #                                  'name': c.name,
        #                                  'value': c.value,
        #                                  'expiry': c.expires,
        #                                  'path': c.path,
        #                                  'httpOnly': False,
        #                                  'HostOnly': False,
        #                                  'sameSite': 'None',
        #                                  'secure': c.secure and True or False}
        else:
            self.__class__.cookie = {'domain': urlx}
        print('COOKIE [ ' + urlx + ' ] = ' + str(self.__class__.cookie))
        driver.add_cookie(self.__class__.cookie)
        # driver.add_cookie(self.__class__.cookies)
        # print('COOKIE BEEN ADDED = ' + str(driver.get_cookie()))
        driver.get(urlone)
        userpage1 = driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
        print('Name of the user = ' + userpage1)
        driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
        driver.find_element_by_xpath("//*[contains(text(), '" + user1 + "')]").click()
        email1 = driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
        join1 = driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
        print('User email = ' + email1)
        print('User Joined date = ' + join1)
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.mengkome_url = driver.current_url
        driver.close()
        # driver.quit()

    def test_99_relogin_then_logout(self):
        # sleep(2)
        print('\n---->  ' + str(self._testMethodName) + '\n')
        urlone = self.__class__.mengkome_url

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-web-security")
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        chrome_options.add_argument("--disable-cookie-encryption")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--test-type")
        ## new one ####
        # experimentalFlags = ['same-site-by-default-cookies@1', 'cookies-without-same-site-must-be-secure@1']
        # chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
        # chrome_options.add_experimental_option('localState', chromeLocalStatePrefs)
        chrome_options.add_experimental_option('prefs', {'credentials_enable_service': True,
                                                         'profile': {'password_manager_enabled': True}})
        ## webdriver section
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)
        # sleep(5)

        driver.get(urlone)
        driver.add_cookie(self.__class__.cookie)
        driver.get(urlone)
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
        if driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
            print('User ' + self.__class__.userone + ' successfully LOGGED OUT')
            print('CURRENT URL = ' + driver.current_url)
        driver.close()
        # driver.quit()

    def tearDown(self):
        # driver.quit()
        print('--- >> TEARDOWN')
        # self.assertEqual([], self.verificationErrors)


    # @classmethod
    def tearDownClass(self):
        print('\n---->  tearDownClass -- ')
        try:
            # sleep(5)
            print(self.__class__.chromedatadir)
            removedir(self.__class__.chromedatadir)
            print('  Successfully remove tmp file ' + self.__class__.chromedatadir)
        except Exception as exx:  # except WindowsError as exx:
            print('Failed to delete directory ' + self.__class__.chromedatadir)
            print('==  Error = ' + str(exx))

if __name__ == "__main__":
    unittest.main()