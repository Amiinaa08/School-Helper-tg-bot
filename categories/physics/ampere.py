from config import bot

def get_magnetic_field_message(message):
    msg = bot.send_message(message.chat.id, 'Введи силу струму')
    bot.register_next_step_handler(msg, I_handler)

def I_handler(message):
    try:
        I = float(message.text)
    except ValueError as err:
        print(err)
    else:
        msg = bot.send_message(message.chat.id, 'Введи відстань до провідника')
        bot.register_next_step_handler(msg, r_handler, I)

def r_handler(message, I):
    try:
        r = float(message.text)
    except ValueError as err:
        print(err)
    else:
        magnetic_filed = get_magnetic_field(I, r)
        bot.send_message(message.chat.id, 'Індукція магнітного поля = {}'.format(magnetic_filed))

def get_magnetic_field(I, r):
    return (4 * 3.14 * 10 ** -7 * I) / (2 * 3.14 * r)