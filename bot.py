import telebot
import config
import random
import requests
import final

#pip install pyTelegramBotAPI
#pip install requests
#pip install Pillow
#pip install bs4
#pip install lxml

from telebot import types
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.TOKEN)
USERS = set()


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")
    item3 = types.KeyboardButton("Тук")
    item4 = types.KeyboardButton('/serfnet')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Oink! Oink! Привет, {0.first_name}! Oink!".format(message.from_user),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def serf(message):
	if message.chat.type == 'private':
		t = 'Тук'
		b = 'Рандомное число'
		c = 'Как дела?'
		d = 'http://'
		bot.send_message(message.chat.id, f'Команда \'{t}\' - специальный скрипт для тренировки барабанщиков.\n Введите \'{t}\' и вам отправят случайную барабанную парчу. \n \'{b}\' - генератор рандомных чисел.\n \'{c}\' - с помощью этой команды можно узнать настроение бота.\n Так же у бота есть функция выгрузки информации с интернет страницы. Для этого просто нужно отправить боту любую ссылку в формате ')



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, f"{str(random.randint(0, 100))} Oink.")
        elif message.text == 'Как дела?':
        	i = random.randint(1, 2)
        	if i == 1:
        		sti = open('stickers/bad.webp', 'rb')
        		bot.send_sticker(message.chat.id, sti)
        		bot.send_message(message.chat.id, 'Я мертв в душе! Oink...')
        	elif i == 2:
        		sti = open('stickers/ok.webp', 'rb')
        		bot.send_sticker(message.chat.id, sti)
        		bot.send_message(message.chat.id, 'Все ок)) Oink!')
        elif message.text == 'Тук':
            final.photo_select()
            with open('someshet.jpg', 'rb') as ph:
            	bot.send_photo(message.from_user.id, photo=ph)
        elif 'www' in message.text or 'http' in message.text:
        	rs = requests.get(message.text)
        	if rs.status_code == 200:
        		root = BeautifulSoup(rs.content, 'html.parser')
        		article = root.select_one('article')
        		sti = open('stickers/rdy.webp', 'rb')
        		bot.send_message(message.chat.id, f'{article.text}')
        		bot.send_sticker(message.chat.id, sti)
        		bot.send_message(message.chat.id, 'Oink!')
        	else:
        		sti = open('stickers/nrdy.webp', 'rb')
        		bot.send_sticker(message.chat.id, sti)
        		bot.send_message(message.chat.id, 'An error occured. Oink. Maybe you wrote a wrong link? Oink.')
        else:
            sti = open('stickers/wha.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Oink?')


bot.polling(none_stop=True)
