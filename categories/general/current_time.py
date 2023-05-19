from config import bot
import datetime

def get_current_time_message(message):
    utc_offset = 3
    now = datetime.datetime.utcnow() + datetime.timedelta (hours=utc_offset)
    time_str = now.strftime ("%H:%M:%S")

    bot.send_message(message.chat.id, 'Зараз такий час - {}'.format(time_str))