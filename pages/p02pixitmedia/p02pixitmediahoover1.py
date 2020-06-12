__author__ = 'carburgess1'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
# import datetime

class P02PixitMediaHoover(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators user infos
    _main_type = 'xpath'
    _first_page = '//*[@id="user-tools"]/strong'
    _users_page = "//*[contains(text(), 'Users')]"

    _user_info_type = 'link'
    _email_info = '//*[@class="form-row field-email"]/*/*[@class="readonly"]'
    _join_date = '//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]'
    # Locators logout
    _logout_tb = "//*[contains(text(), 'Log out')]"
    _logout_chk = "//*[@id='content']/h1"

    # PixitMedia page


    ## General
    def returnCurrentURL(self):
        return self.driver.current_url

    def gotosite(self, URL):
        return self.driver.get(URL)

    def returnDomainFrURL(self, url):
        return str(url.split('://')[1].split('/')[0])
