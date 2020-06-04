# Selenium_Python3_Cookie_Auth
Selenium Automation with cookie authentication

## 1) MengKome (Rosli_Talib Django)
### https://mengkome.pythonanywhere.com/ 

Assignment 1 (Test1) :

- Go to main page https://mengkome.pythonanywhere.com/
- Login (with test user - username / passwd = bacaone / qawsed123456 )
- Logout and keep/save Cookie (make sure it's usable)
- Relogin (automatically) mengkome (same page before logout) using Cookie
- Check some infos inside 
  - go & click Users button
  - click at your username
  - check email address & date joined
- Logout
- Relogin again (automatically) using Cookie
  - go back to home page
- Logout - make sure now Cookie is expired or not usable anymore

## 1.1) Basic UnitTest :

To run :

### python3 UnitTests/test2_login_logout_diffwindows_chromeopts_three.py

## 1.2) pytest Automation Framework

MengKome Automation Framework consise these directories:

1) apps
2) base
3) configfiles
4) features
5) pages
6) tests
7) utilities
8) logs
9) screenshots (screenshot's pictures - create automatically if ERROR occured)

To run tests (example) :

### py.test -v -s tests/p01mengkome/p01mengkomeloginout1_test1.py --browser "$browser"

"$browser" = [ ie / chrome / firefox / opera ]
