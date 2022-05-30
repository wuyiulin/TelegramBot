import os
import sys
import re
import configparser
import telegram.ext
import requests
import time


import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# Initial bot by Telegram access token

config = configparser.ConfigParser()
config.read('config.ini')


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def getUID(update, context):
    update.message.reply_text(update['message']['chat']['id'])
    print(update['message']['chat']['id'])

def Alert():
    TOKEN = config.get('Bot','ACCESS_TOKEN')
    UID = config.get('Bot','UID')
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    text ='實驗跑完啦！快上來收數據！'
    dp.bot.send_message(chat_id=UID, text=text) # 發送訊息


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    
    TOKEN = config.get('Bot','ACCESS_TOKEN')
    UID = config.get('Bot','UID')
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("Alert", Alert))
    dp.add_handler(CommandHandler("getUID", getUID))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
