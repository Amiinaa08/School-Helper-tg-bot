from config import bot

def get_starlight_information_message(message):
  bot.send_message(message.chat.id, 'Освітленість зоряного світла збігається з мінімальною освітленістю людського ока (~0,1 млк), тоді як місячне світло збігається з мінімальною освітленістю людського ока для колірного зору (~50 млк)..')
