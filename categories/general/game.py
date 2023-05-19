from config import bot
import random

STORIES = [
    """Велику чорну собаку звали {}. Два хлопчика, Миколка і Іванко, підібрали його {}. 

{} вони йшли лісом. Пес біг попереду. Хлопчики гаряче сперечалися {}.

– Собака моя, – казав Миколка, – я перший побачив песика і підібрав його!

– Ні, моя, – сердився Іванко, – я перев’язував йому лапу і носив для нього смачні шматочки!

Ніхто не хотів поступитися. Хлопчики сильно посварилися, {}""",
"""Марічка йшла додому після школи, як раптом бачить - на вулиці лежить {}. Вона одразу схопила його та заховала {}. 
- Коли ти повернеш це назад? - запитувала мама Марічки.
-  {}, - впевнено відповідала їй донька. Але сама розуміла, що не зробить цього ніколи, {}.
І сталося так, що {}, та Марічка була щаслива."""
]

def get_game_message(message):
    msg = bot.send_message(message.chat.id, 'Введи "хто"')
    bot.register_next_step_handler(msg, person_handler)


def person_handler(message):
    person = message.text
    msg = bot.send_message(message.chat.id, 'Введи "де"')
    bot.register_next_step_handler(msg, place_handler, person)


def place_handler(message, person):
    place = message.text
    msg = bot.send_message(message.chat.id, 'Введи "коли"')
    bot.register_next_step_handler(msg, time_handler, person, place)


def time_handler(message, person, place):
    time = message.text
    msg = bot.send_message(message.chat.id, 'Введи "навіщо"')
    bot.register_next_step_handler(msg, reason_handler, person, place, time)


def reason_handler(message, person, place, time):
    reason = message.text
    msg = bot.send_message(message.chat.id, 'Введи "що"')
    bot.register_next_step_handler(msg, story_handler, person, place, time, reason)


def story_handler(message, person, place, time, reason):
    result = message.text
    story = random.choice(STORIES).format(person, place, time, reason, result)
    bot.send_message(message.chat.id, story)
