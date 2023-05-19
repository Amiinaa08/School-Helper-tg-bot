from config import bot

def get_circle_square_message(message):
    msg = bot.send_message(message.chat.id, 'Введи радіус кола')
    bot.register_next_step_handler(msg, radius_handler)

def radius_handler(message):
    try:
        radius = float(message.text)
    except ValueError as err:
        print(err)
    else:
        circle_square = get_circle_square(radius)
        bot.send_message(message.chat.id, 'Площа кола - {}'.format(circle_square))


def get_circle_square(radius):
    return 3.14 * radius ** 2