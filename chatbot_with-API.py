import telebot
import json
import requests


# API_TOKEN='5890357652:AAH0Q6hKziZqCiPtL0JKw-qJQIuhmqmuZmk'



API_URL ='https://7012.deeppavlov.ai/model'
API_weather ='1623cbad619822a9010dbdf4f6886918'

with open("name.txt","r",encoding="utf-8") as fh:API_TOKEN=fh.readline()
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Готов к работе!")
    bot.send_message(message.chat.id, "Я бот-умник и знаю целых 2(!) команды!")
    bot.send_message(message.chat.id, "/wiki - обо всем на свете")
    bot.send_message(message.chat.id, "/weather - погода в городах мира (правда писать придется по-английски")

@bot.message_handler(commands=['wiki'])
def wiki(message):

    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")


@bot.message_handler(commands=['weather'])
def weather(message):
    s=''
    s_city = message.text.split()[1:]
    # city_id = 0
    #
    # try:
    #     res = requests.get("http://api.openweathermap.org/data/2.5/find",
    #                        params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': API_weather})
    #     data = res.json()
    #     cities = ["{} ({})".format(d['name'], d['sys']['country'])
    #               for d in data['list']]
    #     print("city:", cities)
    #     city_id = data['list'][0]['id']
    #     print('city_id=', city_id)
    # except Exception as e:
    #     print("Exception (find):", e)
    #     pass
    # # city_id = message.text.split()[1:]
    # print(city_id)
    s = (f'City: {s_city[0]}')
    print(s)
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID':API_weather})

        data = res.json()
        print(data)

        # print("conditions:", data['weather'][0]['description'])
        # print("temp:", data['main']['temp'])

        s=(f'City: {str(s_city)}')
        bot.send_message(message.chat.id, s)
        s=(f"conditions: {data['weather'][0]['description']}")

        bot.send_message(message.chat.id,s)

        s=(f"temp: {data['main']['temp']}")

        bot.send_message(message.chat.id,s)

    except Exception as e:
        bot.send_message(message.chat.id,"Exception (weather):", e)
        pass



bot.polling()