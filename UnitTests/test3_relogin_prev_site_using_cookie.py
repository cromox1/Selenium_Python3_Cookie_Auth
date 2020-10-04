'''
WORK FOR BELOW WEBSITES (AT THE MOMENT):
1) github.com -- > cookie['name'] = 'user_session'
2) mengkome.pythonanywhere.com (my DJango website) -- > cookie['name'] = 'sessionid'
3) cwjobs.co.uk -- > cookie['name'] = 'wrSessionId'
4) totaljobs.com -- > cookie['name'] = 'wrSessionId'
5)
'''
import browser_cookie3
import time
import glob, os

def extract_cookie(cookie_file=None, domainname=""):
    domaincookies = browser_cookie3.chrome(cookie_file=cookie_file, domain_name=domainname)
    cookielist = []
    if domainname == "":
        print()
        if len(domaincookies) >= 1:
            print('[No]) [Domainname] / [Name] / [Value] / [Expires]')
            i = 1
            for c in domaincookies:
                timeexpire = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(c.expires))
                print(str(i) + ') ' + str(c.domain) + ' / ' + str(c.name) + ' / ' + str(c.value) + ' / ' + str(timeexpire))
                i = i + 1
        else:
            print('COOKIE [ all_domain ] = NONE')
        cookielist = [{'domain': 'None', 'expires': 0, 'secure': 0}]
    else:
        if len(domaincookies) >= 1:
            i = 1
            if len(domaincookies) > 1:
                # print('[No])  [Name]  /  [Expires]  /  [Value] \n')
                print('[No])  [Name]  /  [Domain]  /  [Value] \n')
            for c in domaincookies:
                cookie = c.__dict__
                if len(domaincookies) == 1:
                    print('1) COOKIE [ ' + str(cookie['name']) + ' / ' + str(
                        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(cookie['expires'])))) + ' ] = ' + str(
                        cookie))
                    cookielist.append(cookie)
                else:
                    if int(cookie['expires']) >= int(time.time()):
                        # print(str(i) + ') ' + str(cookie['name']) + ' / ' + str(
                        #     time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(cookie['expires'])))) + ' / ' + str(
                        #     cookie['value']))
                        print(str(i) + ') ' + str(cookie['name']) + ' / ' + str(cookie['domain']) + ' / ' + str(
                            cookie['value']))
                        cookielist.append(cookie)
                        i = i + 1
        else:
            print('COOKIE [ ' + domainname + ' ] = NONE')
            cookielist = [{'domain': 'None', 'expires': 0, 'secure': 0}]
    return cookielist

def browserDriver(browser='chrome'):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    print('\n--- > start browser')
    if browser=='brave':
        brave_exe=r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
        chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        chrome_options.add_argument("--disable-cookie-encryption")
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument("--test-type")
        chrome_options.binary_location = brave_exe
        driver = webdriver.Chrome(chromedriverpath, options=chrome_options)
    else:
        from platform import system as osname
        if (osname() == 'Windows'):
            chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        elif (osname() == 'Linux'):
            chromedriverpath = '/opt/google/chromedriver/chromedriver'
        else:
            chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        chrome_options.add_argument("--disable-cookie-encryption")
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument("--test-type")
        driver = webdriver.Chrome(chromedriverpath, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    print('--- > browser driver now ready\n')
    return driver

def choosedomaincookie(cookielist):
    cookie = {'domain': 'None', 'expires': 0, 'secure': 1}
    if len(cookielist) == 1:
        cookie = cookielist[0]
    else:
        yourdomain = input('Choose Cookie [ 1 - ' + str(len(cookielist)) + ' ] : ')
        try:
            if int(yourdomain) <= len(cookielist) and int(yourdomain) > 0:
                cookie = cookielist[int(yourdomain) - 1]
            else:
                print('  -- > WRONG SELECTION - Out Of Range')
        except:
            print('  -- > WRONG SELECTION - Not An Integer')
    return cookie

print()
print('\n-- > > Specific Domainname ---- \n')
yourdomain = input('Your domainname = ')
print('\n  -- > domainname = ' + yourdomain + '\n')
cookielist = []
brave_cookiefile = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies'))[0]
print('BRAVE_COOKIEFILE = ' + str(brave_cookiefile))
chrome_cookiefile = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\Cookies'))[0]
print('CHROME_COOKIEFILE = ' + str(chrome_cookiefile))
# for cfile in [str(chrome_cookiefile), str(brave_cookiefile)]:
for cfile in [str(chrome_cookiefile)]:
    cookielist = cookielist + extract_cookie(cfile, yourdomain)
# print('COOKIELIST 1 = ' + str(cookielist))
print()
cookie1 = choosedomaincookie(cookielist)
if cookie1['secure'] == 0:
    cookie1['secure'] = False
elif cookie1['secure'] == 1:
    cookie1['secure'] = True
else:
    cookie1['secure'] = True

## Browse section - only use Chrome or Brave only
if cookie1['expires'] > 0:
    driver = browserDriver()
    urlx = 'https://' + cookie1['domain'] + cookie1['path']
    print('URL = ' + str(urlx))
    try:
        driver.get(urlx)
        print('COOKIE = ' + str(cookie1))
        driver.add_cookie(cookie1)
        driver.get(urlx)
        url1 = driver.current_url
        print('ULR1 = ' + str(url1))
        # then you can do whatever you want to do here
        # to check wheter login or not
        time.sleep(10)
        url2 = driver.current_url
        print('ULR2 = ' + str(url2))
        if url2 != url1:
            print('--- > SUCCESS !!!')
        else:
            print('--- > FAILED !!!')
            driver.quit()
    except Exception as e:
        print('  Error -- > ' + e.__str__())
        driver.quit()
elif cookie1['expires'] == 0 and cookie1['secure'] == True:
    print()
else:
    print('Domain has no cookie or cookie has expired')