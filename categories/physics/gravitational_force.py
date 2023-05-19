from config import bot

def get_gravitational_force_message(message):
    msg = bot.send_message(message.chat.id, 'Введи масу об\'єкту')
    bot.register_next_step_handler(msg, mass_handler)

def mass_handler(message):
    try:
        mass = float(message.text)
    except ValueError as err:
        print(err)
    else:
        gravitational_force = get_gravitational_force(mass)
        bot.send_message(message.chat.id, 'Сила тяжіння - {}'.format(gravitational_force))


def get_gravitational_force(mass):
    return mass * 9.8