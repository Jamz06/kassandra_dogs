import requests

def telegram_bot_sendtext(bot_message):

   bot_token = '5023228206:AAF2sn6EM3FeKVhV8vm4CYHvCRR7tgT26fc'
   bot_chatID = '413200158'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

if __name__ == '__main__':
    telegram_bot_sendtext('Test')