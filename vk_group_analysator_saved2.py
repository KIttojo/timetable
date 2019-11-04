import vk_api
import time
import random

def main():
    VK = vk_api.VkApi(token = 'aa56c8233e0b89dd0e67cd1cb04bcffaa791606ae2c039abd1af4f40306b543afa3cd308c8c87d87b9317')

    try:
        get_chat = VK.method("messages.getConversations", { "count": 1, "filter":'unanswered'})
        get_id_1 = get_chat['items'][0]['last_message']['from_id']
        first_mes_1 = random.randint(100000, 10000000)
        print(VK.method("messages.send", {"random_id": first_mes_1,"user_id": get_id_1, "message": "Для начала работы с ботом напишите в чат !start .В дальнейшем следуйте инструкциям, которые будут даны вам при правильном прохождении этапов мини-квеста"}))

    except:
        print("Imput is empty")
    
    while True:
        get_chat = VK.method("messages.getConversations", { "count": 1, "filter":'unanswered'})
        
        
        try:
            get_id = get_chat['items'][0]['last_message']['from_id']
            now_text = get_chat['items'][0]['last_message']['text']
            first_mes = random.randint(100000, 10000000)

            f = open('text.txt', 'w')
            f.write(now_text)
            
            if now_text == '!stop': #stopping the code
                return False 
            
        except :
            print("...")

if __name__ == '__main__':
    main()

