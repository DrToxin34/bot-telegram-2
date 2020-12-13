import telebot
import random
import requests
import bs4

def gif_nemo():
	'''Парсит ссылки с гифками немо'''
	# Подключаемся к сайту с гифками Nemo 
	res = requests.get('https://tenor.com/search/nemo-gifs')
	# Проверяем подключение к сайту 404- ошыбка, 200 - ок
	res.raise_for_status()
	# Скачиваем файл .html
	soup = bs4.BeautifulSoup(res.text)

	gifElem = soup.select('img[src]')
	gif_list =  []
	for i in gifElem:
		gifUrl = i.get('src')
		gif_list.append(gifUrl)
	return gif_list
	
def gif_csgo():
	'''Парсит ссылки с гифками немо'''
	# Подключаемся к сайту с гифками Nemo 
	res = requests.get('https://tenor.com/search/csgo-gifs')
	# Проверяем подключение к сайту 404- ошыбка, 200 - ок
	res.raise_for_status()
	# Скачиваем файл .html
	soup = bs4.BeautifulSoup(res.text)

	gifElem = soup.select('img[src]')
	gif_list =  []
	for i in gifElem:
		gifUrl = i.get('src')
		gif_list.append(gifUrl)
	return gif_list
	
bot = telebot.TeleBot('1463314892:AAFyea2e6nR9Dbv86QK6TsqxBk-hEm5-kIc')


@bot.message_handler(commands=['start'])
def start_message(message) :
	keyboard = telebot.types.ReplyKeyboardMarkup(True)
	keyboard.row('привет', 'как дела?', 'gif csgo ')
	keyboard.row('пока', 'скинь мем', 'gif рыба')
	bot.send_message(message.chat.id, 'Боже, народний карась України у телеграмі', reply_markup=keyboard)
	print(message)
	
@bot.message_handler(content_types=['text'])
def send_text(message):
	if 'привет' == message.text:
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM-X7pCZoRL4cKDP8Mo30VvsSweudsAAlUCAAJWnb0KrEssgk-jFd8eBA')
	elif 'пока'in message.text.lower():
		bot.send_message(message.chat.id, 'Не здохни')
	elif 'мем'in message.text.lower():
		bot.send_message(message.chat.id, 'https://steamuserimages-a.akamaihd.net/ugc/85970797296227631/C8871AB3E0353D6E02A39577ADF574149B11B3E8/')
	elif 'дела' in message.text.lower():
		bot.send_message(message.chat.id, 'Четко')
		bot.send_sticker(message.chat.id, 'https://steamuserimages-a.akamaihd.net/ugc/85970797296227631/C8871AB3E0353D6E02A39577ADF574149B11B3E8/')
	elif 'рыба'in message.text.lower():
		bot.send_message(message.chat.id, random.choice(gif_nemo()))
	elif 'csgo'in message.text.lower():
		bot.send_message(message.chat.id, random.choice(gif_csgo()))

bot.message_handler(content_types=['sticker'])
def send_sticker(message):
	print(message.sticker.file_id)
	
	
bot.polling() 
	
