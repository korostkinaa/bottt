from dicts import *
from telebot import types
import random
chats = {}




def start_game(bot, chat_id):
    chats[chat_id] = {}
    chats[chat_id]['step'] = 0
    keyb = types.InlineKeyboardMarkup()
    bot.send_message(chat_id, "Начало игры", reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(chat_id, description, reply_markup=keyb.add(
        types.InlineKeyboardButton("Нажите, чтобы учавстовать", callback_data="MyGame|Go")))


# -----------------------------------------------------------------------
def callback_worker(bot, cur_user, cmd, par, call):
    chat_id = call.message.chat.id
    message_id = call.message.id

    if cmd == "Go":
        chats.update({call.message.chat.id: {call.from_user.username: 0, "num": None, "catch": True, 'step': 0}})
        print(chats)
        initilaze_dict(bot, chat_id)

    elif cmd == "IDK":
        keyboard = types.InlineKeyboardMarkup()
        [keyboard.add(types.InlineKeyboardButton(button, callback_data="MyGame|Var|1")) for button in QA["variants"]]
        bot.send_message(chat_id, f'*{QA["variants"]}*', reply_markup=keyboard, parse_mode='Markdown')
        keyb = types.InlineKeyboardMarkup()
        bot.send_message(chat_id, QA["variants"],
                         reply_markup=keyb.add(types.InlineKeyboardButton("1", callback_data="MyGame|IDK")))
        bot.send_message(chat_id,
                         f'Какие вы ТУПЫЕ.\nОтвет: *{QA[chats[chat_id]["num"]]["right"]}*',
                         parse_mode='Markdown')
        chats[call.message.chat.id][call.from_user.username] -= 1
        initilaze_dict(bot, chat_id)
    elif cmd == "Var":
        keyboard = types.InlineKeyboardMarkup()
        bot.send_message(id, random.choice(phrase),
                     reply_markup=keyb.add(types.InlineKeyboardButton("Вариант 1", callback_data="MyGame|IDK")))
        keyboard = types.InlineKeyboardMarkup()
        bot.send_message(id, random.choice(phrase),
                     reply_markup=keyb.add(types.InlineKeyboardButton("Вариант 2", callback_data="MyGame|IDK")))
        keyboard = types.InlineKeyboardMarkup()
        bot.send_message(id, random.choice(phrase),
                     reply_markup=keyb.add(types.InlineKeyboardButton("Вариант 3", callback_data="MyGame|IDK")))
        keyboard = types.InlineKeyboardMarkup()
        bot.send_message(id, random.choice(phrase),
                     reply_markup=keyb.add(types.InlineKeyboardButton("Вариант 4", callback_data="MyGame|IDK")))


def initilaze_dict(bot, id):
    chats[id]['step'] += 1
    randomize = chats[id]['step']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    [keyboard.add(types.KeyboardButton(button)) for button in QA[randomize]["variants"]]
    bot.send_message(id, f'*{QA[randomize]["caption"]}*', reply_markup=keyboard, parse_mode='Markdown')
    keyb = types.InlineKeyboardMarkup()
    bot.send_message(id, random.choice(phrase),
                     reply_markup=keyb.add(types.InlineKeyboardButton("Я не знаю...", callback_data="MyGame|IDK")))

    chats[id]["num"] = randomize

def catch_error(bot, chat_id):
    try:
        return chats[bot, chat_id]['catch']
    except KeyError:
        return False

def check_answer(bot,message):
    print(chats)
    if message.text.lower() == QA[chats[message.chat.id]["num"]]['right'].lower() and chats[message.chat.id][
        message.from_user.username] < 15:
        chats[message.chat.id][message.from_user.username] += 1
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEE0qpijyo37rRJf3zjguFKa7EPFUvlCgACEAMAAm2wQgOS41nh81K2aSQE")
        bot.send_message(message.chat.id, f"Отличная работа @*{message.from_user.username}*!!!!", parse_mode='Markdown')
        initilaze_dict(message.chat.id)
    elif chats[message.chat.id][message.from_user.username] == 2:
        bot.send_message(message.chat.id, f"ПОЗДРАВЛЯЮ С ПОБЕДОЙ! @{message.from_user.username}!!!!",
                         parse_mode='Markdown')
        chats[message.chat.id] = {}

