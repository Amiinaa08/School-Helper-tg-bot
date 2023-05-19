from config import bot

def get_earth_form_message(message):
  bot.send_message(message.chat.id, 'Форма Землі - геоїд.')
