from telebot import TeleBot
from dotenv import dotenv_values

# Config Variables
CONFIG = dotenv_values()

bot = TeleBot(CONFIG['API_KEY'])
