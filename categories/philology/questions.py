from config import bot

def get_question_rule_message(message):
  bot.send_message(message.chat.id, 'Питальне слово + допоміжне (або модальне) дієслово + підмет + присудок + додаток + інші члени речення.')
