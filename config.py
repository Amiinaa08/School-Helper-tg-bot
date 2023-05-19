from dotenv import load_dotenv
import telebot
import os
# from telethon.sync import TelegramClient

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# for saving txt
# API_ID = os.getenv("API_ID")
# API_HASH = os.getenv("API_HASH")
# client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
