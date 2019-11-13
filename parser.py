# -*- coding: utf-8 -*-
import urllib.request
import vk_api
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
with urllib.request.urlopen('http://ictis.sfedu.ru/rasp/HTML/39.htm') as url: s = url.read()

def find_day(soup, needed_day):
	print("find_day")
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
		# else: 
		# 	print(f"!!!{day[4:]}!={needed_day}!!!")
		# 	print(len(day[4:]), len(needed_day))
	find_timetable(soup, indx)

def find_timetable(soup, indx):
	print("find_timetable()")
	try:
		file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\timetable.txt', 'w')
		name_box2 = soup.findAll('font', attrs={'size': "1"})

		for x in name_box2[indx*9:indx*9+8]:
			buff = x
			buff = buff.text.strip()
			buff = buff.replace("_", "") #to delete all "_" from output

			file.write(buff)
			# file.write("\n") теперь почему-то не высылаются в лс в вк сообщения ВК, содержащие перенос строк
			print(buff)

	except:
		print("Введите корректный день.")

def main_f():
	soup = BeautifulSoup(s, 'html.parser')
	#code starts below
	# needed_day = 'Птн,27  сентября '
	day_file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\day.txt', 'r', encoding='utf-8')
	needed_day = day_file.readline()
	print(needed_day)
	find_day(soup, needed_day)
