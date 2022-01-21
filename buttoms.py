from telebot import types

keyMain = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
buttonBuy = types.KeyboardButton("✅Купить")
buttonAdmin = types.KeyboardButton("🏴Админ")
keyMain.add(buttonBuy, buttonAdmin)