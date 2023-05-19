from config import bot
import random

def get_rand_num_message(message):
  rand_num = random.randint (1, 100)
  bot.send_message(message.chat.id, 'Вам випало число {}'.format(rand_num))