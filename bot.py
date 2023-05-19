from telebot import types
from config import bot
import random

from constants import APP_HIERARCHY, RATE_JUDGEMENTS, GENERAL_CATEGORY_QUOTE, Categories, Commands

begin_message_id = ""
chat_id = ""
current_category = Categories.MAIN_MENU

def set_current_category(current_category_input):
    global current_category
    current_category = current_category_input

def find_function(text):
    if text == Categories.MAIN_MENU:
        return welcome
    for category in APP_HIERARCHY:
        if category["name"] == text:
            subcategory_list = [subcategory["name"] for subcategory in category["subcategories"]]
            return subcategory_list
        for subcategory in category["subcategories"]:
            if subcategory["name"] == text:
                return subcategory["function"]

    return "Вибач, я не знаю цієї теми."

def get_element_parent(text):
    if text == Categories.MAIN_MENU:
        return Categories.MAIN_MENU
    for category in APP_HIERARCHY:
        if category["name"] == text:
            return Categories.MAIN_MENU
        subcategory_list = [subcategory["name"] for subcategory in category["subcategories"]]
        if text in subcategory_list:
            return category["name"]


def handle_message_text(message_text, message):
    if message_text.lower() == Commands.HELP.lower():
        help(message)
        return
    if message_text.lower() == Commands.BACK.lower():
        back(message)
        return
    if message_text.lower() == Commands.QUIT.lower():
        quit(message)
        return

    result = find_function(message_text)
    if type(result) is list:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        args = []
        for subcategory_name in result:
            args.append(subcategory_name)
        markup.add(*args)
        markup.add(*[Commands.BACK, Commands.HELP, Commands.QUIT])
        
        set_current_category(message_text)
        
        if message_text == Categories.GENERAL:
            bot.send_message(
            message.chat.id,
            GENERAL_CATEGORY_QUOTE.format(message_text),
            reply_markup=markup,
        )
        else:
            bot.send_message(
                message.chat.id,
                random.choice(RATE_JUDGEMENTS).format(message_text),
                reply_markup=markup,
            )
    elif type(result) is str:
        bot.send_message(message.chat.id, result)
    else:
        result(message)

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    args = []
    for category in APP_HIERARCHY:
        args.append(category["name"])
    markup.add(*args)
    markup.add(*[Commands.HELP, Commands.QUIT])
    
    set_current_category(Categories.MAIN_MENU)
    
    global begin_message_id 
    begin_message_id = message.message_id
    global chat_id
    chat_id = message.chat.id

    bot.send_message(
        message.chat.id,
        "Вітаю, {0.first_name}!\nЯ - <b>{1.first_name}</b>, готовий допомогти тобі з домашнім завданням.".format(
            message.from_user, bot.get_me()
        ),
        parse_mode="html",
        reply_markup=markup,
    )

@bot.message_handler(commands=["quit"])
def quit(message):
    global current_category
    current_category = Categories.MAIN_MENU
    bot.send_message(
        message.chat.id,
        "До побачення, {0.first_name}! Був радий з тобою поспілкуватись!".format(message.from_user),
    )

@bot.message_handler(commands=["back"])
def back(message):
    handle_message_text(get_element_parent(current_category), message)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(
        message.chat.id,
        "Ви обрали '{}'. Для виходу, напишіть '/quit'. Для повернення до останньої теми напишіть '/back'.".format(current_category),
    )

@bot.message_handler(content_types=["text"])
def message(message):
    if message.chat.type == "private":
        handle_message_text(message.text, message)


bot.polling(none_stop=True)

# TODO?: add dialog save to txt file
