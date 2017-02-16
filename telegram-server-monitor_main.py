#!/usr/bin/env python3

import configparser as cp
from telegram.ext import Updater
import logging
import os

config = []
alarms = []
reports = []

class Alarm(object):
    _init_(self):
        self.type = []
        self.theshold = []
        self.above = True
        self.uid = ""

class Report(object):
    _init_(self):
        self.type = []
        self.freqency = 0
        self.start = 0
        self.uid = ""

def check_whitelist(func):
    def func_wrapper(*args, **kwargs):

        global config

        def dummy(*xargs, **xkwargs):
            return

        # check if username is in the whitelist
        if args[1].message.user.username in config['WHITELIST']:
            return func(*args, **kwargs)
        else:
            return dummy(*args, **kwargs)


def read_config():
    config = cp.ConfigParser()
    try:
        config.read('/etc/telegram-server-monitor/whitelist.conf')
    except:
        exit(1)
    print(config)
    return config

@check_whitelist
def reload(bot, update):
    global config
    config = read_config()

@check_whitelist
def help(bot, update):
    text = """Telegram Server Monitor Bot
Commands:
/help       - This message
/status     - Send server status
/report n   - Send recurring status message every n minutes, with the first one right now
/report off - Disable sending recurrent status messages
/alarm disk device percentage
            - Send alarm message if disk 'device' exceeds 'percentage' fill level
/alarm disk off
            - Disable disk level alarm
/alarm cpu load
            - Send alarm message if cpu load exceeds 'load'
/alarm cpu off
            - Disable cpu load alarm
/reload     - Reload config and whitelist
/quit       - quit bot
    """
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

@check_whitelist
def status(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Dummy status")

@check_whitelist
def reload(bot, update):
    read_config()
    bot.sendMessage(chat_id=update.message.chat_id, text="Reloaded")

@check_whitelist
def report(bot, update):
    read_config()
    bot.sendMessage(chat_id=update.message.chat_id, text="Reloaded")

@check_whitelist
def alarm(bot, update):
    read_config()
    bot.sendMessage(chat_id=update.message.chat_id, text="Reloaded")

#def quit(bot, update):








updater = Updater(token=config['TOKEN'])
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher

read_whitelist()

from telegram.ext import CommandHandler
start_handler = CommandHandler('help', help)
start_handler = CommandHandler('status', status)
# start_handler = CommandHandler('report', report, pass_args=True)
# start_handler = CommandHandler('alarm', alarm, pass_args=True)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle(stop_signals=(2, 15, 6))
