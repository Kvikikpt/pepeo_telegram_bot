import telebot
import config
import random
import requests
import final

#pip install pyTelegramBotAPI
#pip install requests
#pip install Pillow

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


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


@bot.message_handler(commands=['serfnet'])
def serf(message):
	if message.chat.type == 'private':
		bot.send_message(message.chat.id, 'Пожалуйста, дай мне ссылку! Oink.')



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, f"{str(random.randint(0, 100))} Oink.")
        elif message.text == 'Как дела?':
            bot.send_message(message.chat.id, 'Я мертв в душе! Oink...')
        elif message.text == 'Тук':
            final.photo_select()
            with open('someshet.jpg', 'rb') as ph:
            	bot.send_photo(message.from_user.id, photo=ph)
        else:
            sti = open('stickers/wha.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Oink?')


bot.polling(none_stop=True)
