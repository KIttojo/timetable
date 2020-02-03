import vk_api
import random
import file1

def main():
	VK = vk_api.VkApi(token = '7bae9726b9b3b04e6c21694562aa1e0f80e0dc0f202afae626f685b9cac3e4021e9aa077e48401c872dbc')

	while True:
		try:
			get_chat = VK.method("messages.getConversations", { "count": 1, "filter":'unanswered'})
			get_id_1 = get_chat['items'][0]['last_message']['from_id']
			first_mes_1 = random.randint(100000, 10000000)
			now_text = get_chat['items'][0]['last_message']['text']

			file = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\timetable.txt', 'r')
			day = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\day.txt', 'w', encoding='utf-8')

			space_indx = list(now_text).index(" ")

			if space_indx<2:
				now_text = "0" + now_text

			for x in range(len(now_text)):
				if now_text[x] == " ":
					formated_text = now_text[:x] + " " + now_text[x:] + " "

			day.write(formated_text)
			file1.main_f()

			file_text = file.readline()
			print(VK.method("messages.send", {"random_id": first_mes_1,"user_id": get_id_1, "message": file_text}))
			file.close()
			day.close()
			print("Конец")
		except:
			print("-")

if __name__ == '__main__':
	main()
