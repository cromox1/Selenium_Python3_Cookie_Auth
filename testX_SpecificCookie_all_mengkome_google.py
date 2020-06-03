from shutil import copy2
from time import sleep, localtime, strftime
from os import remove as removefile
import browser_cookie3

def extract_cookie(domainname=""):
    ## Location of Cookie file (specific location + file)
    filepath = 'chromedata\\Default\\'
    file = 'Cookies'
    cookiefile = filepath + file
    cookietemp = filepath + 'mytmp123'
    print('\nCOOKIE_EXE_FILE = ' + str(cookiefile))
    copy2(src=cookiefile, dst=cookietemp)
    sleep(1)
    cookies = browser_cookie3.chrome(domain_name=domainname, cookie_file=cookietemp)
    if domainname == "":
        if len(cookies) >= 1:
            print('[No]) [Domainname] / [Name] / [Value] / [Expires]')
            i = 1
            for c in cookies:
                timeexpire = strftime('%Y-%m-%d %H:%M:%S', localtime(c.expires))
                print(str(i) + ') ' + str(c.domain) + ' / ' + str(c.name) + ' / ' + str(c.value) + ' / ' + str(timeexpire))
                i = i + 1
        else:
            print('COOKIE [ all_domain ] = NONE')
        cookie = {}
    else:
        if len(cookies) >= 1:
            cookie = {}
            for c in cookies:
                # cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}
                cookie = {'domain': c.domain,
                          'name': c.name,
                          'value': c.value,
                          'expiry': c.expires,
                          'path': c.path,
                          'httpOnly': False,
                          'HostOnly': False,
                          'sameSite': 'None',
                          'secure': c.secure and True or False}
            print('COOKIE [ ' + domainname + ' / ' + str(
                strftime('%Y-%m-%d %H:%M:%S', localtime(cookie['expiry']))) + ' ] = ' + str(cookie))
        else:
            print('COOKIE [ ' + domainname + ' ] = NONE')
            cookie = {}
    sleep(1)
    removefile(cookietemp)
    return cookie

# ## Location of Cookie file (specific location + file)
# cookie_exefile = 'chromedata\\Default\\Cookies'
# print('\nCOOKIE_EXE_FILE = ' + str(cookie_exefile))

# 1) ALL COOKIES
extract_cookie()

# 2) mengkome COOKIES
base_url = "https://mengkome.pythonanywhere.com/admin/login/"
print('\n-- > > URL ' + base_url + ' ---- ')
urlx = str(base_url.split('://')[1].split('/')[0])
print('URLX = ' + urlx)
# urlx = '.pythonanywhere.com'
# urlx = 'mengkome.pythonanywhere.com'
extract_cookie(urlx)

# 3) google COOKIES
print('\n-- > > URL .google.com ---- ')
extract_cookie('.google.com')
