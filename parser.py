import urllib.request
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

with urllib.request.urlopen('http://ictis.sfedu.ru/rasp/HTML/39.htm') as url: s = url.read()

soup = BeautifulSoup(s, 'html.parser')

needed_day = 'Птн,01  ноября '
#нахождение дня денели и запись в переменную
table = soup.findAll('font', attrs={'size': '2'})
# print(table)

for x in table: #тут мы получили список дат. Ищем нужную, берем индекс и выводим дни, используя индекс
	time_table = ''
	day = x.find('p').text
	if day == needed_day:
		time_table = x
		indx = table.index(time_table)
		print(indx) #доставем индекс элемента, чтобы потом достать его из 119 записей
	print(f'day={day}, needed_day={needed_day}')

for i in range(1):
 	# print(soup.findAll('tr', attrs={'class': 'question-hyperlink'}, limit=2)) вывод предметов в один день
 	name_box2 = soup.findAll('font', attrs={'size': "1"})
 	print(name_box2)
 	for x in range(indx*8, indx*8 + 6):
 		buff = name_box2[x]
 		buff = buff.text.strip()
 		print(buff)
