import vk_api
import time
import random

def main():
    VK = vk_api.VkApi(token = 'aa56c8233e0b89dd0e67cd1cb04bcffaa791606ae2c039abd1af4f40306b543afa3cd308c8c87d87b9317')

    while True:
        try:
            get_chat = VK.method("messages.getConversations", { "count": 1, "filter":'unanswered'})
            get_id_1 = get_chat['items'][0]['last_message']['from_id']
            first_mes_1 = random.randint(100000, 10000000)
            now_text = get_chat['items'][0]['last_message']['text']

            text = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\timetable.txt', 'r')
            day = open('C:\\Users\\denis\\Desktop\\Python 3\\parser\\day.txt', 'w', encoding='utf-8')

            day.write(now_text)

            # print(VK.method("messages.send", {"random_id": first_mes_1,"user_id": get_id_1, "message": text}))



        except:
            print("Imput is empty")


if __name__ == '__main__':
    main()
