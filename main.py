from telebot import TeleBot
from dotenv import dotenv_values
import requests

# Config Variables
CONFIG = dotenv_values()

bot = TeleBot(CONFIG['API_KEY'])
@bot.message_handler(commands=['start'])

def hello_word(messege):
    data = requests.get('https://api.github.com/users/r0h9m')

    print(type(data.json()))
    bot.send_message(messege.chat.id,'koni')

bot.polling()