from config import bot

def get_verb_rule_message(message):
  bot.send_message(message.chat.id, 'Ніяк! В українській мові відмінки мають лише іменники, прикметники та займенники.')
