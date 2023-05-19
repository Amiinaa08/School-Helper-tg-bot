from config import bot
import math

def get_distance_message(message):
    msg = bot.send_message(message.chat.id, 'Введи x точки')
    bot.register_next_step_handler(msg, x1_handler)

def x1_handler(message):
    try:
        x1 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи y точки')
        bot.register_next_step_handler(msg, y1_handler, x1)

def y1_handler(message, x1):
    try:
        y1 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи z точки')
        bot.register_next_step_handler(msg, z1_handler, x1, y1)

def z1_handler(message, x1, y1):
    try:
        z1 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        P = {'x': x1, 'y': y1, 'z': z1}
        msg = bot.send_message(message.chat.id, 'Введи x першої точки на прямій')
        bot.register_next_step_handler(msg, x2_handler, P)

def x2_handler(message, P):
    try:
        x2 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи y першої точки на прямій')
        bot.register_next_step_handler(msg, y2_handler, P, x2)

def y2_handler(message, P, x2):
    try:
        y2 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи z першої точки на прямій')
        bot.register_next_step_handler(msg, z2_handler, P, x2, y2)

def z2_handler(message, P, x2, y2):
    try:
        z2 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        A = {'x': x2, 'y': y2, 'z': z2}
        msg = bot.send_message(message.chat.id, 'Введи x другої точки на прямій')
        bot.register_next_step_handler(msg, x3_handler, P, A)

def x3_handler(message, P, A):
    try:
        x3 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи y другої точки на прямій')
        bot.register_next_step_handler(msg, y3_handler, P, A, x3)

def y3_handler(message, P, A, x3):
    try:
        y3 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи z другої точки на прямій')
        bot.register_next_step_handler(msg, z3_handler, P, A, x3, y3)

def z3_handler(message, P, A, x3, y3):
    try:
        z3 = float(message.text)
    except ValueError as err:
        print(err)
    else:
        B = {'x': x3, 'y': y3, 'z': z3}
        distance = get_distance(P, A, B)
        bot.send_message(message.chat.id, 'Відстань - {}'.format(distance))


def get_distance(P, A, B):
    fraction_top = math.fabs((P['x'] - A['x']) * (P['x'] - B['x']) + (P['y'] - A['y']) * (P['y'] - B['y']) + (P['z'] - A['z']) * (P['z'] - B['z']))
    fraction_bottom = math.sqrt(math.pow(B['x'] - A['x'], 2) + math.pow(B['y'] - A['y'], 2) + math.pow(B['z'] - A['z'], 2))
    return fraction_top / fraction_bottom