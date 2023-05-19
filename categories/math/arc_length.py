from config import bot

def get_arc_length_message(message):
    msg = bot.send_message(message.chat.id, 'Введи радіус кола')
    bot.register_next_step_handler(msg, a_handler)

def a_handler(message):
    try:
        a = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи кут між двома точками на колі')
        bot.register_next_step_handler(msg, b_handler, a)

def b_handler(message, a):
    try:
        b = float(message.text)
    except ValueError as err:
        print(err)
    else:
        lenght = get_arc_length(a, b)
        bot.send_message(message.chat.id, 'Довжина дуги кола - {}'.format(lenght))


def get_arc_length(a, b):
    return a * b