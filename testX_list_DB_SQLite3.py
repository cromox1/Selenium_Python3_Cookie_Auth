import glob
import os
import sqlite3
from time import sleep
from shutil import copy2

def listing_SQLite3_DB(filepath, file, DBtable):
    print('\nDB FILE = ' + filepath + file)
    copy2(src=filepath+file, dst=filepath+'mytmp123')
    sleep(1)
    con = sqlite3.connect(filepath + 'mytmp123')
    cur = con.cursor()
    sqlcommand = "SELECT * FROM " + str(DBtable)
    print('SQL req = ' + sqlcommand + '\n')
    cur.execute(sqlcommand)
    names = [description[0] for description in cur.description]
    print(str(names) + '\n')
    rows = cur.fetchall()
    if len(rows) >= 1:
        i = 1
        for row in rows:
            print(str(i) + ') ' + str(row))
            i = i+1
    else:
        print('SQLTABLE ' + DBtable + ' EMPTY - NO DATA')
    sleep(1); con.close(); sleep(1)
    os.remove(filepath+'mytmp123')

# filepath
##########
# 1) Chrome Default
# -- > /cygdrive/c/Users/taverner/AppData/Local/Google/Chrome/User Data/Default
# filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\'))[0]
# 2) chrome specific directory - chromedata
# -- > 'C:\\Users\\penggunabiasa\\python3_projects\\Selenium\\MengKome\\chromedata\\Default\\Cookies'
# filepath = 'chromedata\\Default\\'

print('\n1) Default Chrome directory')
print('2) Specific - chromedata\Default')
pathchoice = input('CHOOSE DIRECTORY/PATH FOR SQLITE3 DB FILE [1-2] : ')

try:
    if str(pathchoice) == str(2) or pathchoice[0].lower() == 's':
        filepath = 'chromedata\\Default\\'
    else:
        filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''),
                                          '..\Local\\Google\\Chrome\\User Data\\Default\\'))[0]
except:
    filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''),
                                      '..\Local\\Google\\Chrome\\User Data\\Default\\'))[0]
print('\nDirectory/Path : ' + filepath + '\n')

# DB file & DB table
####################

print('1) Cookie DB')
print('2) Login Data DB')
print('3) History DB - visits')
print('4) History DB - urls')
print('5) Web Data DB - autofill')
print('6) Web Data DB - token_service')
print('7) Web Data DB - autofill_profiles')
print('8) Web Data DB - credit_cards')
print('9) Web Data DB - unmasked_credit_cards')
print('10) Web Data DB - masked_credit_cards')
dbchoice = input('CHOOSE DB & TABLE TO QUERY [1-10] : ')

try:
    if str(dbchoice) == str(2) or dbchoice[0].lower() == 'l':
        file = 'Login Data'; dbtable = 'logins'
    elif str(dbchoice) == str(3) or dbchoice[0].lower() == 'v':
        file = 'History'; dbtable = 'visits'
    elif str(dbchoice) == str(4) or dbchoice[0].lower() == 'u':
        file = 'History'; dbtable = 'urls'
    elif str(dbchoice) == str(5) or dbchoice[0].lower() == 'a':
        file = 'Web Data'; dbtable = 'autofill'
    elif str(dbchoice) == str(6) or dbchoice[0].lower() == 't':
        file = 'Web Data'; dbtable = 'token_service'
    elif str(dbchoice) == str(7) or dbchoice[0].lower() == 'p':
        file = 'Web Data'; dbtable = 'autofill_profiles'
    elif str(dbchoice) == str(8) or dbchoice[0].lower() == 'c':
        file = 'Web Data'; dbtable = 'credit_cards'
    elif str(dbchoice) == str(9):
        file = 'Web Data'; dbtable = 'unmasked_credit_cards'
    elif str(dbchoice) == str(10) or dbchoice[0].lower() == 'm':
        file = 'Web Data'; dbtable = 'masked_credit_cards'
    else:
        file = 'Cookies'; dbtable = 'cookies'
except:
    file = 'Cookies'; dbtable = 'cookies'

# EXECUTE command to check the DB
listing_SQLite3_DB(filepath, file, dbtable)



