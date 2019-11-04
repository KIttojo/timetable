# -*- coding: utf-8 -*-

import urllib.request
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

with urllib.request.urlopen('http://ictis.sfedu.ru/rasp/HTML/39.htm') as url: s = url.read()
soup = BeautifulSoup(s, 'html.parser')
#code starts below
# needed_day = 'Птн,27  сентября '
day_file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\day.txt', 'r', encoding='utf-8')
needed_day = day_file.readline()
print(needed_day)

table = soup.findAll('font', attrs={'size': '2'})

for x in table: #finding index of needed week and saving it in "indx" variable
    time_table = ''
    day = x.find('p').text

    if day == needed_day:
        time_table = x
        indx = table.index(time_table)
        break
#if we found date, we'll save timetable for this day
try:
    file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\timetable.txt', 'w')
    name_box2 = soup.findAll('font', attrs={'size': "1"})

    for x in name_box2[indx*9:indx*9+8]:
        buff = x
        buff = buff.text.strip()

        file.write(buff)
        print(buff)

except:
    print("Введите корректный день.")
