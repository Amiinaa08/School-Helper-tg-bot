from config import bot

def get_two_countries_names_message(message):
  bot.send_message(message.chat.id, 'росія та Китай. Кожна з цих держав межує ще з 14 іншими країнами. Бажаєш дізнатися, з якими саме?')
#   bot.register_next_step_handler(msg, countries_names_handler)

# def countries_names_handler(message):
#   text = message.text.lower()
#   if text == "так":
#     bot.send_message(message.chat.id, "")