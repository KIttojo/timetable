# -*- coding: utf-8 -*-
import urllib.request
import vk_api
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
with urllib.request.urlopen('http://ictis.sfedu.ru/rasp/HTML/39.htm') as url: s = url.read()

def find_day(soup, needed_day):
	print("\nfinding day")
	# soup = BeautifulSoup(s, 'html.parser')
	# day_file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\day.txt', 'r', encoding='utf-8')
	# needed_day = day_file.readline()

	table = soup.findAll('font', attrs={'size': '2'})

	for x in table: #finding index of needed week and saving it in "indx" variable
		time_table = ''
		day = x.find('p').text

		if day[4:] == needed_day:
			time_table = x
			indx = table.index(time_table)
			break
		else: 
			error = "Попробуйте ввести другой день."

	find_timetable(soup, indx, error)

def find_timetable(soup, indx, error):
	print("finding timetable")
	if (error != None):
		print("День не НаН")
		file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\timetable.txt', 'w')
		try:
			name_box2 = soup.findAll('font', attrs={'size': "1"})

			for x in name_box2[indx*9:indx*9+8]:
				buff = x
				buff = buff.text.strip()
				buff = buff.replace("_", "") #to delete "_" from the end of line
				print(buff)

				file.write(buff)

				print(buff)
		except:
			file.write("Пар нет, отдыхайте.")

	else:
		print("Неверная дата")
		file.write(error)

	file.close()


def main_f():
	soup = BeautifulSoup(s, 'html.parser')
	day_file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\day.txt', 'r', encoding='utf-8')
	needed_day = day_file.readline()
	find_day(soup, needed_day)
	day_file.close()
