__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
from time import strftime, sleep
# from requests import get as urlget
# from PyPDF2 import PdfFileReader as PDFread
# from os import remove as removefile
from selenium.webdriver.common.action_chains import ActionChains as hoover

class TestOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n--- > setUpClass\n')

    def setUp(self):
        print('\n--- > setUp\n')
        # self.driver = webdriver.Firefox()
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
        # self.tmpfilename = 'tmptest123.pdf'

    def test_one(self):
        driver = self.driver
        current1 = strftime("%Y-%m-%d %H:%M:%S")
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('q').click()
        driver.find_element_by_name('q').send_keys("pixitmedia" + Keys.ENTER)
        list_pixitmedia = driver.find_elements_by_xpath("//*[contains(text(),'Pixit Media')]")
        # OLD code - not working anymore
        # for element in list_pixitmedia:
        #     if element.text == "https://www.pixitmedia.com/":
        #         element.click()
        # if driver.find_element_by_xpath("//*[contains(text(),'https://www.pixitmedia.com/')]").text == "https://www.pixitmedia.com/":
        #     driver.get("https://www.pixitmedia.com/")
        list_pixitmedia[0].click()
        basepixitmediaurl = driver.current_url
        print('PIXITMEDIA URL = ' + str(basepixitmediaurl))
        element_pixstor = driver.find_elements_by_xpath("//*[contains(text(),'PixStor')]")[0]
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

        # Full Page scroll down
        # driver.find_element_by_xpath("//*[contains(text(),'Contact Us')]").send_keys(Keys.PAGE_DOWN)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTo(0, Y)")
        # Half page scroll down
        last_height = self.displayheight()
        one_height = int(0.5 * last_height)
        print('0.5HEIGHT = ' + str(one_height))

        driver.find_elements_by_xpath("//*[contains(text(),'Data Sheets')]")[0].click()
        driver.execute_script("window.scrollTo(0, " + str(one_height) + ");")
        sleep(2)
        pixstor_overview = driver.find_elements_by_xpath("//*[contains(text(),'PixStor Overview')]")
        if len(pixstor_overview) >= 1:
            print('PixStor Overview pdf FOUND!!!')
            print('Element text = ' + str(pixstor_overview[0].text))
            pixstor_overview[0].click()
        else:
            print('PixStor Overview NOT FOUND')

        # # View Datasheet - PDF file -- NOW NO LONGER EXIST !!!!
        # driver.find_element_by_xpath("//span[@class='elementor-button-text']").click()
        #
        # ## validate PDF file
        # currenturl = driver.current_url
        # req = urlget(currenturl)
        # # validate1 - simple by check header
        # self.assertGreater(int(req.headers['Content-Length']), 1000)
        # self.assertEqual(req.headers['Content-Type'], 'application/pdf')
        # # validate2 - download & check file using PyPDF2
        # file1 = open(self.tmpfilename, "wb")
        # file1.write(req.content)
        # pdfproducer = PDFread(self.tmpfilename).getDocumentInfo().producer
        # file1.close()
        # pdfchklist = ['Adobe', 'PDF', 'Acrobat']  # words to confirm PDF
        # listintrsect = [x.upper() for x in pdfchklist if x.upper() in pdfproducer.upper()]
        # self.assertGreaterEqual(len(listintrsect), 1)

        # Contact Us Form
        driver.get(basepixitmediaurl)
        driver.find_element_by_xpath("//*[contains(text(),'Contact Us')]").click()
        # print("URL Contact Us = " + str(driver.current_url))

        driver.execute_script("window.scrollTo(0, " + str(one_height) + ");")
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
        message1 = "This is a test for Jez \nToday is " + str(current2) + \
                   '\nExact testing time : From ' + str(current1) + ' to ' + str(current2) + \
                   "\nThis Earth of Mankind (Bumi Manusia) - is it Jez?? I don't think so"
        print('MESSAGE :\n' + str(message1))
        element_message.send_keys(message1)
        # Half page scroll down
        driver.execute_script("window.scrollTo(0, " + str(one_height) + ");")
        driver.find_element_by_name('input_8.1').click()
        element_send = driver.find_element_by_xpath("//*[@value='Send']")
        hoover(driver).move_to_element(element_send).perform()
        element_send.click()

    def tearDown(self):
        print('\n--- > tearDown\n')
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        # try:
        #     removefile(self.tmpfilename)
        #     # print('  Successfully remove tmp file ' + str(self.tmpfilename))
        # except WindowsError as exx:
        #     print('  Error = ' + str(exx) + ' / file = ' + str(self.tmpfilename))

    @classmethod
    def tearDownClass(cls):
        print('\n--- > tearDownClass\n')

    def displayheight(self):
        driver = self.driver
        try:
            last_height = driver.execute_script("return document.body.scrollHeight")
        except:
            last_height = 1800
        if last_height <= 1800:
            last_height = 1850
        print('HEIGHT = ' + str(last_height))
        return last_height

if __name__ == "__main__":
    unittest.main()
