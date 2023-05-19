from config import bot

def get_rectangle_square_message(message):
    msg = bot.send_message(message.chat.id, 'Введи першу сторону прямокутника')
    bot.register_next_step_handler(msg, a_handler)

def a_handler(message):
    try:
        a = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи другу сторону прямокутника')
        bot.register_next_step_handler(msg, b_handler, a)

def b_handler(message, a):
    try:
        b = float(message.text)
    except ValueError as err:
        print(err)
    else:
        square = get_rectangle_square(a, b)
        bot.send_message(message.chat.id, 'Площа прямокутника - {}'.format(square))


def get_rectangle_square(a, b):
    return a * b