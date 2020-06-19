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

def extract_cookie(domainname=""):
    domaincookies = browser_cookie3.chrome(domain_name=domainname)
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
        cookielist = [{'domain': 'None', 'expires': 0}]
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
            cookielist = [{'domain': 'None', 'expires': 0}]
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
    cookie = {'domain': 'None', 'expires': 0}
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
cookielist = extract_cookie(yourdomain)
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
        # then you can do whatever you want to do here
    except Exception as e:
        print('  Error -- > ' + e.__str__())
        driver.quit()
else:
    print('Domain has no cookie or cookie has expired')
