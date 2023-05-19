from config import bot

def get_biggest_ocean_message(message):
  bot.send_message(message.chat.id, 'Тихий океан. Його площа становить 165 200 000 км²')
    