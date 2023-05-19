from config import bot

import datetime
def get_current_year_message(message):
  today = datetime.date.today()
  year = today.year
  bot.send_message(message.chat.id, 'Сьогодні такий рік - {}'.format(year))