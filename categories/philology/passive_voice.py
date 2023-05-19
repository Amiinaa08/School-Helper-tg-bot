from config import bot

def get_passive_voice_rule_message(message):
  bot.send_message(message.chat.id, 'Схема побудови пасивного стану в Present Simple буде наступною. Предмет / людина + am / are / is + 3-тя форма неправильного дієслова або правильний дієслово з закінченням -ed.')
