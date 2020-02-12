# -*- coding: utf-8 -*-
import urllib.request

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
with urllib.request.urlopen('http://ictis.sfedu.ru/rasp/HTML/39.htm') as url: s = url.read()

def find_day(soup, needed_day):
	print("\nfinding day")

	table = soup.findAll('font', attrs={'size': '2'})
	matches = 0;
	#находим индекс нужной нам недели
	for x in table: 

		time_table = ''
		day = x.find('p').text

		if day[4:] == needed_day:
			time_table = x
			indx = table.index(time_table)
			matches+=1
			break

	find_timetable(soup, indx, matches)

def find_timetable(soup, indx, matches):
	#используя найденный нами индекс, вытаскиваем расписание на этот день
	file = open('DIR\\timetable.txt', 'w')
	
	try:
		name_box2 = soup.findAll('font', attrs={'size': "1"})

		for x in name_box2[indx*9:indx*9+8]:
			buff = x
			buff = buff.text.strip()
			buff = buff.replace("_", "") #удаляем "_" с конца строк

			file.write("|  ") #чтобы отделять расписание пар
			file.write(buff)

	except:
		file.write("Пар нет, отдыхайте.")

	file.close()


def main_f():
	soup = BeautifulSoup(s, 'html.parser')

	day_file = open('DIR\day.txt', 'r', encoding='utf-8')
	needed_day = day_file.readline()

	find_day(soup, needed_day)
	day_file.close()
