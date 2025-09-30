from telebot import TeleBot
from dotenv import dotenv_values

TOKEN = dotenv_values['API_KEY']

bot = TeleBot(TOKEN)