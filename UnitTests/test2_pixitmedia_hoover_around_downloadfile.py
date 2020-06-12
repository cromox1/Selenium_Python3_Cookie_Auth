__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
from time import strftime, sleep
from os import remove as removefile
import fleep
import wget

from selenium.webdriver.common.action_chains import ActionChains as hoover

class TestHooverPixitMedia(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n--- > setUpClass\n')

    def setUp(self, browser='chrome'):
        print('\n--- > setUp\n')
        # self.driver = webdriver.Firefox()
        if browser=='brave':
            brave_exe=r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
            self.chromedriverpath = r'C:\tools\chromedriver\chromedriver_v81.exe'
            self.chrome_options = Options()
            self.chrome_options.add_argument('--ignore-certificate-errors')
            self.chrome_options.add_argument("--disable-web-security")
            self.chrome_options.add_argument("--incognito")
            self.chrome_options.add_argument("--allow-running-insecure-content")
            self.chrome_options.add_argument("--allow-cross-origin-auth-prompt")
            self.chrome_options.add_argument("--disable-cookie-encryption")
            self.chrome_options.add_argument('--disable-dev-shm-usage')
            self.chrome_options.add_argument("--test-type")
            self.chrome_options.binary_location = brave_exe
            ## webdriver section
            self.driver = webdriver.Chrome(self.chromedriverpath, options=self.chrome_options)
            # pass
        else:
            self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
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
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.co.uk"
        self.verificationErrors = []
        self.tmpfilename = 'tmptest123.pdf'

    def test_one(self):
        driver = self.driver
        current1 = strftime("%Y-%m-%d %H:%M:%S")
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('q').click()
        driver.find_element_by_name('q').send_keys("pixitmedia" + Keys.ENTER)
        list_pixitmedia = driver.find_elements_by_xpath("//*[contains(text(),'Pixit Media')]")
        self.assertGreaterEqual(len(list_pixitmedia), 1)

        # OLD code - not working anymore
        # for element in list_pixitmedia:
        #     if element.text == "https://www.pixitmedia.com/":
        #         element.click()
        # if driver.find_element_by_xpath("//*[contains(text(),'https://www.pixitmedia.com/')]").text == "https://www.pixitmedia.com/":
        #     driver.get("https://www.pixitmedia.com/")
        list_pixitmedia[0].click()
        basepixitmediaurl = driver.current_url
        print('PIXITMEDIA URL = ' + str(basepixitmediaurl))
        elements_pixstor = driver.find_elements_by_xpath("//*[contains(text(),'PixStor')]")
        self.assertGreaterEqual(len(elements_pixstor), 1)

        element_pixstor = elements_pixstor[0]
        hoover(driver).move_to_element(element_pixstor).perform()
        features_el = driver.find_element_by_xpath("//*[contains(text(),'Features')]")
        hoover(driver).move_to_element(features_el).perform()
        powersearch_el = driver.find_element_by_xpath("//*[contains(text(),'Powerful Search')]")
        hoover(driver).move_to_element(powersearch_el).perform()
        powersearch_el.click()

        driver.get(basepixitmediaurl)
        element_comp = driver.find_elements_by_xpath("//*[contains(text(),'Company')]")[0]
        hoover(driver).move_to_element(element_comp).perform()
        resc_el = driver.find_element_by_xpath("//*[contains(text(),'Resources')]")
        hoover(driver).move_to_element(resc_el).perform()
        resc_el.click()
        if driver.find_elements_by_xpath("//*[contains(text(),'Data Sheets')]"):
            driver.execute_script("window.scrollTo(0, " + str(self.displayheight()[2]) + ");")
            driver.find_elements_by_xpath("//*[contains(text(),'Data Sheets')]")[0].click()
        else:
            driver.find_elements_by_xpath("//*[contains(text(),'Data Sheets')]")[0].click()
        driver.execute_script("window.scrollTo(0, " + str(self.displayheight()[1]) + ");")
        sleep(2)
        pixstor_overview = driver.find_elements_by_xpath("//*[contains(text(),'PixStor Overview')]")
        if len(pixstor_overview) >= 1:
            print('PixStor Overview PDF FOUND!!!')
            print('Element text = ' + str(pixstor_overview[0].text))
            pixstor_overview[0].click()
            # View Datasheet - PDF file
            if driver.find_element_by_xpath("//*[contains(text(),'DOWNLOAD')]"):
                driver.execute_script("window.scrollTo(0, " + str(self.displayheight()[2]) + ");")
            pdffileurl = driver.find_element_by_xpath("//*[contains(text(),'DOWNLOAD')]").get_attribute('href')
            print('PDF FILE URL = ' + str(pdffileurl))
            # validate PDF file
            wget.download(pdffileurl, out=self.tmpfilename)
            file1 = open(self.tmpfilename, "rb")
            chkfile = fleep.get(file1.read(128))
            # print('TYPE = ' + str(chkfile.type))
            print('EXTN = ' + str(chkfile.extension))
            print('MIME = ' + str(chkfile.mime))
            self.assertIn('pdf', str(chkfile.mime))
            file1.close()
        else:
            print('PixStor Overview PDF NOT FOUND')

        # Contact Us Form
        driver.get(basepixitmediaurl)
        driver.find_element_by_xpath("//*[contains(text(),'Contact Us')]").click()
        # print("URL Contact Us = " + str(driver.current_url))

        driver.execute_script("window.scrollTo(0, " + str(self.displayheight()[1]) + ");")
        # All data to send
        name1 = 'Cromox'
        name2 = 'One'
        email1 = 'bumimanusia@gmail.com'
        comp1 = 'Ranorexxx'
        phone1 = "07769916425"
        subject1 = 'Test1'
        print('NAME : ' + name1 + ' ' + name2)
        print('EMAIL : ' + email1 + ' / PHONE : ' + phone1)
        print('COMPANY : ' + comp1)
        print('SUBJECT : ' + str(subject1))
        # fill-in the form
        element_firstname = driver.find_element_by_name('input_1.3')
        hoover(driver).move_to_element(element_firstname).perform()
        element_firstname.clear()
        element_firstname.send_keys(name1)
        element_lastname = driver.find_element_by_id("input_2_1_6")
        hoover(driver).move_to_element(element_lastname).perform()
        # element_lastname.click()
        element_lastname.clear()
        element_lastname.send_keys(name2)
        element_email = driver.find_element_by_id("input_2_2")
        hoover(driver).move_to_element(element_email).perform()
        # element_email.click()
        element_email.clear()
        element_email.send_keys(email1)
        element_company = driver.find_element_by_id("input_2_3")
        hoover(driver).move_to_element(element_company).perform()
        element_company.clear()
        element_company.send_keys(comp1)
        element_phone = driver.find_element_by_id("input_2_7")
        hoover(driver).move_to_element(element_phone).perform()
        element_phone.clear()
        element_phone.send_keys(phone1)
        element_subject = driver.find_element_by_id("input_2_4")
        hoover(driver).move_to_element(element_subject).perform()
        element_subject.clear()
        element_subject.send_keys(subject1)
        element_message = driver.find_element_by_id("input_2_6")
        hoover(driver).move_to_element(element_message).perform()
        element_message.clear()
        current2 = strftime("%Y-%m-%d %H:%M:%S")
        message1 = "This is a test for Jez \n\nToday is " + str(current2) + \
                   '\nExact testing time : From ' + str(current1) + ' to ' + str(current2) + \
                   "\nThis Earth of Mankind (Bumi Manusia) -> is it Jez?? " \
                   "\nI don't think so. Look at the inconsiderate you!!"
        print('MESSAGE :\n' + str(message1))
        element_message.send_keys(message1)
        # Half page scroll down
        driver.execute_script("window.scrollTo(0, " + str(self.displayheight()[1]) + ");")
        driver.find_element_by_name('input_8.1').click()
        element_send = driver.find_element_by_xpath("//*[@value='Send']")
        self.assertIsNotNone(element_send)
        hoover(driver).move_to_element(element_send).perform()
        element_send.click()

    def tearDown(self):
        print('\n--- > tearDown\n')
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        try:
            removefile(self.tmpfilename)
            # print('  Successfully remove tmp file ' + str(self.tmpfilename))
        except WindowsError as exx:
            print('  Error = ' + str(exx) + ' / file = ' + str(self.tmpfilename))

    @classmethod
    def tearDownClass(cls):
        print('\n--- > tearDownClass\n')

    def displayheight(self):
        # Page scroll down
        # driver.find_element_by_xpath("//*[contains(text(),'Contact Us')]").send_keys(Keys.PAGE_DOWN)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTo(0, Y)")
        driver = self.driver
        try:
            last_height = driver.execute_script("return document.body.scrollHeight")
        except:
            last_height = 1800
        if last_height <= 1800:
            last_height = 1850
        half_height = int(0.5 * last_height)
        quater_height = int(0.1 * last_height)
        print('HEIGHT = ' + str(last_height) + ' / 0.5HEIGHT = ' + str(half_height) + ' / 0.1HEIGHT = ' + str(quater_height))
        return last_height,half_height,quater_height

if __name__ == "__main__":
    unittest.main()