__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from os import walk as walkdir
from os.path import join as joinname
from time import sleep
import unittest
import pickle

class TestMengkome1(unittest.TestCase):
    mengkome_url = ''
    cookies = []
    # cookiefile = None
    chromedatadir = "chrome-data"
    userone = 'bacaone'
    pswdone = 'qawsed123456'

    def setUp(self):
        chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        # self.driver = webdriver.Firefox()
        chrome_options = Options()
        # chrome_options.add_argument("user-data-dir=selenium")
        # chrome_options.add_argument("user-data-dir=chrome-data")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--disable-plugins-discovery")
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument("--proxy-server='direct://'")
        # chrome_options.add_argument("--proxy-bypass-list=*")
        print("CHROME_OPTIONS = " + str(chrome_options.arguments))
        self.driver = webdriver.Chrome(chromedriverpath, options=chrome_options)
        self.driver.implicitly_wait(10)
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.verificationErrors = []

    def test_one_login(self):
        # global cookiefile
        cookiefile = None
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        driver = self.driver
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['version'])  # Python 3.7 and below
        # print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion']) # Python 3.8 & above
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
        ## read cookie data and put to cookies variable at the top of the class
        # preferencesfile = "Preferences"
        # cookiesfile_r = open(self.__class__.chromedatadir + '/\Default/\/' + preferencesfile, "rb")
        # print("COOKIESFILE = " + str(cookiesfile_r))
        # self.__class__.cookies = pickle.load(cookiesfile_r)
        # print('COOKIES = ' + str(self.__class__.cookies))
        # cookiesfile_r.close()
        # sleep(2)
        files = []
        preferencesfile = "Preferences"
        for dirpath, dirname, filename in walkdir(self.__class__.chromedatadir):
            for file in filename:
                if file == preferencesfile:
                    files.append(joinname(dirpath, file))
        cookiefile = files[0]
        print("COOKIEFILE = " + str(cookiefile))
        fopenfile = open(str(cookiefile), 'r')
        lines = fopenfile.readlines()
        # self.__class__.cookies = pickle.load(fopenfile)
        self.__class__.cookies = [x for x in lines]
        fopenfile.close()
        sleep(2)
        print('COOKIES = ' + str(self.__class__.cookies))

        ## current URL
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.mengkome_url = driver.current_url

    def test_two_relogin_chkinfos(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.userone
        urlone = self.__class__.mengkome_url
        driver = self.driver

        driver.get(urlone)

        # for cookie in self.__class__.cookies:
        #     if 'expiry' in cookie:
        #         cookie['expiry'] = int(cookie['expiry'])
        #     driver.add_cookie(cookie)
        # sleep(1)
        # driver.get(urlone)

        # print("COOKIES = " + str(self.__class__.cookies))
        # driver.get_cookie(self.__class__.cookies)
        # driver.get(urlone)
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

    def test_x_relogin_then_logout(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        driver = self.driver
        urlone = self.__class__.mengkome_url
        driver.get(urlone)
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
        if driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
            print('User ' + self.__class__.userone + ' successfully LOGGED OUT')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()