import browser_cookie3
import time

def extract_cookie(domainname=""):
    # cookies = browser_cookie3.chrome(domain_name=urlx, cookie_file='C:/Users/cromox/Desktop/newselenium/Selenium/MengKome/chrome-data/Default/Cookies')
    cookies = browser_cookie3.chrome(domain_name=domainname)
    cookiex = []
    if domainname == "":
        print()
        if len(cookies) >= 1:
            print('[No]) [Domainname] / [Name] / [Value] / [Expires]')
            i = 1
            for c in cookies:
                timeexpire = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(c.expires))
                print(str(i) + ') ' + str(c.domain) + ' / ' + str(c.name) + ' / ' + str(c.value) + ' / ' + str(timeexpire))
                i = i + 1
        else:
            print('COOKIE [ all_domain ] = NONE')
        cookiex = ['None']
    else:
        if len(cookies) >= 1:
            # cookie = {}
            i = 1
            for c in cookies:
                # OLD STYLE
                # cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'expiry': c.expires, 'path': c.path,
                #             'httpOnly': False, 'HostOnly': False, 'sameSite': 'None', 'secure': c.secure and True or False}
                cookie = c.__dict__
                if len(cookies) == 1:
                    print('COOKIE [ ' + domainname + ' / ' + str(
                        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(cookie['expires'])))) + ' ] = ' + str(
                        cookie))
                    cookiex.append(cookie)
                else:
                    if int(cookie['expires']) >= int(time.time()):
                        print(str(i) + ') COOKIE [ ' + domainname + ' / ' + str(
                            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(cookie['expires'])))) + ' ] = ' + str(cookie))
                        cookiex.append(cookie)
                        i = i + 1
        else:
            print('COOKIE [ ' + domainname + ' ] = NONE')
            cookiex = ['None']
    return cookiex

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
# print('\n-- > > URL .google.com ---- ')
# extract_cookie('.google.com')

# 4) specific domain
print()
print('\n-- > > Specific Domainname ---- \n')
yourdomain = input('Your domainname = ')
print('\n  -- > domainname = ' + yourdomain + '\n')
extract_cookie(yourdomain)

