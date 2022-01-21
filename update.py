import time
import os
import telebot

def updategit(message, bot):
    bot.send_message(chat_id=message.chat.id, text='Начинаем обновление репозитория на гитхабе (~70 секунд)')
    time.sleep(1)
    cd = os.getcwd()
    os.system('cd ' + str(cd))
    bot.send_message(chat_id=message.chat.id, text='cd ' + str(cd))
    time.sleep(5)
    os.system('git init')
    time.sleep(10)
    os.system('git add .')
    time.sleep(10)
    os.system('git rm -f --cached mytoken.py')
    time.sleep(10)
    os.system('git commit -m "new member"')
    time.sleep(10)
    os.system('git pull origin main')
    time.sleep(10)
    os.system('git push -u origin main')
    time.sleep(10)
    bot.send_message(chat_id=message.chat.id, text='Репозиторий на гитхабе обновлен')