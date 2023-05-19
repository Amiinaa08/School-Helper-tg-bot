from config import bot

def get_heisenberg_equation_message(message):
    msg = bot.send_message(message.chat.id, 'Введи похибку вимірювання положення частинки')
    bot.register_next_step_handler(msg, delta_x_handler)

def delta_x_handler(message):
    try:
        delta_x = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи похибку вимірювання її імпульсу')
        bot.register_next_step_handler(msg, delta_p_handler, delta_x)

def delta_p_handler(message, delta_x):
    try:
        delta_p = float(message.text)
    except ValueError as err:
        print(err)
    else:
        isValid = is_heisenberg_equation_valid(delta_x, delta_p)
        bot.send_message(message.chat.id, 'Рівняння вірне? - {}'.format(isValid))

def is_heisenberg_equation_valid(delta_x, delta_p):
    return delta_x * delta_p >= (6.62607015 * 10 ** -34) / 2