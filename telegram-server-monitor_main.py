from telegram.ext import Updater
import logging

whitelist = []

def read_whitelist():
    try:
        file_handle = open('/etc/telegram-statusbot/whitelist.conf')
    except:
        return
    whitelist = file_handle.readlines()
    file_handle.close()

def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")





updater = Updater(token='')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher

read_whitelist()

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

