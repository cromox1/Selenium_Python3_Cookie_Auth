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
    # sqlcommand = "SELECT * FROM " + str(DBtable)
    sqlcommand = "SELECT * FROM " + str(DBtable) + ' WHERE "host_key" = "www.pythonanywhere.com"'
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
print('2) Default Brave directory')
print('3) Specific - chromedata\Default')
pathchoice = input('CHOOSE DIRECTORY/PATH FOR SQLITE3 DB FILE [1-3] : ')

try:
    if str(pathchoice) == str(3) or pathchoice[0].lower() == 's':
        filepath = 'chromedata\\Default\\'
    elif str(pathchoice) == str(2) or pathchoice[0].lower() == 'b':
        filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''),
                                                  '..\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\'))[0]
    else:
        filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''),
                                          '..\Local\\Google\\Chrome\\User Data\\Default\\'))[0]

except:
    filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''),
                                      '..\Local\\Google\\Chrome\\User Data\\Default\\'))[0]
print('\nDirectory/Path : ' + filepath + '\n')

# DB file & DB table
####################

file = 'Cookies'; dbtable = 'cookies'

# EXECUTE command to check the DB
listing_SQLite3_DB(filepath, file, dbtable)



