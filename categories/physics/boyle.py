from config import bot
from telebot import types

def get_boyle_mariotte_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*["Обчислення P1", "Обчислення V1"])
    msg = bot.send_message(
        message.chat.id,
        "Оберіть категорію",
        reply_markup=markup,
    )
    bot.register_next_step_handler(msg, category_pick_handler)


def category_pick_handler(message):
    category = message.text
    msg = bot.send_message(message.chat.id, 'Введи P2')
    bot.register_next_step_handler(msg, P2_handler, category)

def P2_handler(message, category):
    try:
        P2 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи V2')
        bot.register_next_step_handler(msg, V2_handler, category, P2)

def V2_handler(message, category, P2):
    try:
        V2 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = ""
        if category == "Обчислення P1":
            msg = bot.send_message(message.chat.id, 'Введи V1')
        elif category == "Обчислення V1":
            msg = bot.send_message(message.chat.id, 'Введи P1')
        bot.register_next_step_handler(msg, last_parameter_handler, category, P2, V2)

def last_parameter_handler(message, category, P2, V2):
    try:
        last_parameter = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = ""
        if category == "Обчислення P1":
            msg = "P1 = {}".format(get_P1(last_parameter, P2, V2))
        elif category == "Обчислення V1":
            msg = "V1 = {}".format(get_V1(last_parameter, P2, V2))
        bot.send_message(message.chat.id, msg)

def get_P1(V1, P2, V2):
    return P2 * V2 / V1

def get_V1(P1, P2, V2):
    return P2 * V2 / P1