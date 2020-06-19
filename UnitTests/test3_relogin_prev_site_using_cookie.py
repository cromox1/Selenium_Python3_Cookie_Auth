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
        cookielist = ['None']
    else:
        if len(domaincookies) >= 1:
            i = 1
            if len(domaincookies) > 1:
                print('[No])  [Name]  /  [Expires]  /  [Value] \n')
            for c in domaincookies:
                cookie = c.__dict__
                if len(domaincookies) == 1:
                    print('1) COOKIE [ ' + str(cookie['name']) + ' / ' + str(
                        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(cookie['expires'])))) + ' ] = ' + str(
                        cookie))
                    cookielist.append(cookie)
                else:
                    if int(cookie['expires']) >= int(time.time()):
                        print(str(i) + ') ' + str(cookie['name']) + ' / ' + str(
                            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(cookie['expires'])))) + ' / ' + str(cookie['value']))
                        cookielist.append(cookie)
                        i = i + 1
        else:
            print('COOKIE [ ' + domainname + ' ] = NONE')
            cookielist = ['None']
    return cookielist

def browserDriver(browser='chrome'):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    print('\n--- > setUp\n')
    if browser=='brave':
        brave_exe=r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
        chromedriverpath = r'C:\tools\chromedriver\chromedriver_v81.exe'
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        chrome_options.add_argument("--disable-cookie-encryption")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--test-type")
        chrome_options.binary_location = brave_exe
        ## webdriver section
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
        chrome_options.add_argument("--test-type")
        ## webdriver section
        driver = webdriver.Chrome(chromedriverpath, options=chrome_options)
    driver.implicitly_wait(10)
    return driver

def choosedomaincookie(mycookielist):
    cookiex = {'domain': 'None', 'expires': 0}
    if len(mycookielist) == 1:
        cookiex = mycookielist[0]
    else:
        yourdomain = input('Choose Cookie [ 1 - ' + str(len(mycookielist)) + ' ] : ')
        try:
            if int(yourdomain) <= len(mycookielist) and int(yourdomain) > 0:
                cookiex = mycookielist[int(yourdomain) - 1]
            else:
                print('  -- > WRONG SELECTION - OUT OF RANGE')
        except:
            print('  -- > WRONG SELECTION - NOT AN INTEGER')
    return cookiex

print()
print('\n-- > > Specific Domainname ---- \n')
yourdomain = input('Your domainname = ')
print('\n  -- > domainname = ' + yourdomain + '\n')
cookielist = extract_cookie(yourdomain)
print()
cookie1 = choosedomaincookie(cookielist)
print('COOKIE = ' + str(cookie1))
