import telebot
from telebot import types

bot = telebot.TeleBot('5063951804:AAEV6ujXzFZNGbZkanYa_tDWEpDG_ygXEfA')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("✅Купить")
    button2 = types.KeyboardButton("🏴Админ")
    markup.add(button1, button2)
    bot.send_message(message.from_user.id, 'Добро пожаловать в бота', reply_markup=markup)


@bot.message_handler(commands='updatedrain')
def updatedrain(message):
    bot.send_message(chat_id=message.chat.id, text='Начинаем обновление репозитория на гитхабе (~50 секунд)')
    time.sleep(1)
    cd = os.getcwd()
    os.system('cd ' + str(cd))
    bot.send_message(chat_id=message.chat.id, text='cd ' + str(cd))
    time.sleep(5)
    os.system('git init')
    time.sleep(10)
    os.system('git add .')
    time.sleep(10)
    os.system('git commit -m "new member"')
    time.sleep(10)
    os.system('git pull origin main')
    time.sleep(10)
    os.system('git push -u origin main')
    time.sleep(10)
    bot.send_message(chat_id=message.chat.id, text= 'Репозиторий на гитхабе обновлен')


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
