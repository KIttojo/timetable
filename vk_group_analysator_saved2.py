import vk_api
import random
import file1

def main():
	VK = vk_api.VkApi(token = 'COMMUNITY_TOKEN')

	while True:
		try:
			get_chat = VK.method("messages.getConversations", { "count": 1, "filter":'unanswered'})
			get_id_1 = get_chat['items'][0]['last_message']['from_id']
			first_mes_1 = random.randint(100000, 10000000)
			now_text = get_chat['items'][0]['last_message']['text']

			file = open('DIRECTORY\\timetable.txt', 'r')
			day = open('SAME_DIRECTORY\\day.txt', 'w', encoding='utf-8')

			space_indx = list(now_text).index(" ")
			#если цифра <10, то добавляем 0 для корректного парсинга
			if space_indx < 2:
				now_text = "0" + now_text
			#форматируем
			for x in range(len(now_text)):
				if now_text[x] == " ":
					formated_text = now_text[:x] + " " + now_text[x:] + " "
			#записываем готовую дату в файл и запускаем парсер
			day.write(formated_text)
			file1.main_f()
			#счтываем результат работы парсера и отправлем в качестве аргумента VK API
			file_text = file.readline()

			print(VK.method("messages.send", {"random_id": first_mes_1,"user_id": get_id_1, "message": file_text}))

			file.close()
			day.close()

		except:
			print("No messages yet.")

if __name__ == '__main__':
	main()
