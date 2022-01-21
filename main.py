import telebot
from telebot import types
import mytoken
import buttoms as keys
import update

bot = telebot.TeleBot(mytoken.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать в бота', reply_markup=keys.keyMain)


@bot.message_handler(commands='updategit')
def updateit(message):
    update.updategit(message, bot)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            print(call.data)
            if call.data == "✅Купить":
                key = types.InlineKeyboardMarkup(row_width=1)
                but = types.InlineKeyboardButton("АВТОРЕГИ", callback_data='АВТОРЕГИ')
                key.add(but)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="🔰 Доступные товары:", reply_markup=key)
            if call.data == "АВТОРЕГИ":
                key = types.InlineKeyboardMarkup(row_width=1)
                but1 = types.InlineKeyboardButton("RAMBLER [0.1 руб/шт]", callback_data='RAMBLER')
                but2 = types.InlineKeyboardButton("НАЗАД", callback_data='✅Купить')
                key.add(but1, but2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="🔰 Доступные автореги: ", reply_markup=key)
            if call.data == "RAMBLER":
                key = types.InlineKeyboardMarkup(row_width=1)
                but1 = types.InlineKeyboardButton("КУПИТЬ", callback_data='RAMBLER_КУПИТЬ')
                but2 = types.InlineKeyboardButton("НАЗАД", callback_data='АВТОРЕГИ')
                key.add(but1, but2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="✉ Автореги рамблер\n\n🍩 Краткое описание:\n0.1 рубля за аккаунт\nSMPT"
                                           ", POP3, IMAP активированы\nВид mail@rambler.ru:password\nПол (Ж)",
                                      reply_markup=key)
            if call.data == "RAMBLER_КУПИТЬ":
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                text = '✉ Автореги рамблер\n\n🍩 Описание:\n0.1 рубля за аккаунт\nSMPT, POP3, IMAP активированы\nВид ' \
                       'mail@rambler.ru:password\nПол (Ж)\n' \
                       'На почте лежит одно письмо о завершении регистрации почты\nВсе почты валидны и пройдены ' \
                       'чекером\nМинимальное количество - 10 штук '
                key = types.InlineKeyboardMarkup(row_width=1)
                but1 = types.InlineKeyboardButton("ПОДТВЕРДИТЬ ПОКУПКУ", callback_data='RAMBLER_КУПИТЬ_ACCEPT')
                but2 = types.InlineKeyboardButton("ОТМЕНА", callback_data="ОТМЕНА")
                key.add(but1, but2)
                bot.send_photo(call.message.chat.id, open('rambler.png', 'rb'), caption=text, reply_markup=key)
            if call.data == "ОТМЕНА":
                bot.delete_message(call.message.chat.id, call.message.message_id)
            if call.data == "RAMBLER_КУПИТЬ_ACCEPT":
                bot.send_message(chat_id=call.message.chat.id, text="Введите количество почт, которое хотите приобрести:")

    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == "✅Купить":
        key = types.InlineKeyboardMarkup(row_width=1)
        but = types.InlineKeyboardButton("АВТОРЕГИ", callback_data='АВТОРЕГИ')
        key.add(but)
        bot.send_message(message.chat.id, "🔰 Доступные товары:", reply_markup=key)
    elif message.text == "🏴Админ":
        bot.send_message(message.chat.id, "🏴 Админ - @blesshydra 🏴")
    else:
        bot.send_message(message.chat.id, 'Не удалось обработать команду')
        bot.send_photo(message.chat.id, 'https://sun9-60.userapi.com/c854216/v854216827/1aff21/vAPEg7e1Yfs.jpg')


bot.polling(none_stop=True)
