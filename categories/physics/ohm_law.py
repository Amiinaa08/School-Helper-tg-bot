from config import bot

def get_amperage_message(message):
    msg = bot.send_message(message.chat.id, 'Введи прикладену напругу')
    bot.register_next_step_handler(msg, U_handler)

def U_handler(message):
    try:
        U = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи електричний опір провідника')
        bot.register_next_step_handler(msg, R_handler, U)

def R_handler(message, U):
    try:
        R = float(message.text)
    except ValueError as err:
        print(err)
    else:
        amperage = get_amperage(U, R)
        bot.send_message(message.chat.id, 'Сила струму - {}'.format(amperage))


def get_amperage(U, R):
    return U / R