# Selenium_Python3_Cookie_Auth

Selenium Automation with cookie authentication

## 1) MengKome (Rosli_Talib Django)
### https://mengkome.pythonanywhere.com/ 

Assignment 1 :

Simple cookie authentication usage

- Go to main page https://mengkome.pythonanywhere.com/
- Login (with test user - username / passwd = bacaone / qawsed123456 )
- Close/Quit browser but keep/save Cookie (make sure it's usable)
- Relogin (automatically) mengkome (same page before browser been closed) using Cookie
- Check some infos inside 
  - go & click Users button
  - click at your username
  - check email address & date joined
- Close/Quit browser again
- Relogin again (automatically) using Cookie
  - go back to home page
- Logout 
  - make sure now Cookie is expired or not usable anymore

## 1.1) Basic UnitTest :

To run :
```bash
python3 UnitTests/test1_login_logout_diffwindows_chromeopts.py
```
## 1.2) pytest Automation Framework

MengKome Automation Framework consise these directories:
1. apps   4. pages   6. configfiles    8. features 
2. base    5. tests    7. utilities    9. logs
3. screenshots (screenshot's pictures - create automatically if ERROR occured)

To run tests (example) :
```bash
py.test -v -s tests/p01mengkome/p01mengkomeloginout1_test1.py --browser "$browser"

"$browser" = [ ie / chrome / firefox / opera ]
```
## 2) Pixit Media
### https://www.pixitmedia.com/

Assignment 2 :

Explore on hoover (mouse moving around from element to element), search, download and validate file 

- Launch Google Website
  - Search for pixitmedia
  - then go to pixitmedia site
- Select PIXSTOR menu link
  - then Features
  - then Powerful Search
- Select the COMPANY menu link
  - then go to Resources
  - Validate that the PixStor Overview DATASHEET button returns a PDF/download
- Select the CONTACT US menu link
  - Fill in the form with your contact details.
  - For the Message text area insert the characters: This is a test for Jez
- Send the form

## 2.1) Basic UnitTest :

To run :
```bash
python3 UnitTests/test2_pixitmedia_hoover_around_downloadfile.py 
```
## 2.2) pytest Automation Framework

To run tests (example) :
```bash
py.test -v -s tests/p01google/p01searchpixitmedia_tests.py --browser "$browser"
```
## 3) (Any website with auth login)
### https://github.com 

Assignment 3 :

Relogin website using valid cookie that found in the Webbrowser's DB

- Go to main page GitHub https://github.com
- Login (with test user - username / passwd = xxxx1 / xxxxx2 )
- Close/Quit browser 
- Find cookie in the Webbrowser's DB (Chrome, Brave, Opera, Firefox, etc...)
- Relogin (automatically) GitHub (same page before browser been closed) using Cookie
- Make sure you're successfully auto login
- Check some infos inside 
  - go & click Users button
  - Close/Quit browser again
- Relogin again (automatically) using Cookie
  - go back to home page
- Logout 
  - make sure now Cookie is expired or not usable anymore

## 3.1) Basic UnitTest :

To run :
```bash
python3 UnitTests/test3_relogin_prev_site_using_cookie.py
```
