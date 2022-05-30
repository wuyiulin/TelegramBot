

這邊完全亂碼，趕著下班懶得處理。

可以先閱讀這裡：https://wuyiulin.blogspot.com/2022/05/telegrambot-python.html#more


首先先安裝一下本文所使用的套件：

pip3 install telegram
pip3 install python-telegram-bot


移到你目前想提醒 Python 程式的目錄底下

cd ~/your_Python_program 
建立 Telegram 機器人的主程式（或是從這裡下載我寫好的）
touch TelegramBot.py寫檔，接著複製貼上就可以了。
vim TelegramBot.py
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

（然後向 BotFather 申請自己的機器人並拿到 Token，這部分可以看別的大大寫的這篇。）

在同目錄底下建立 config.ini
touch config.ini
寫 config.ini
vim config.ini把 your_token 換成你剛剛拿到的 TOKEN，
UID 待會再教你拿：
[Bot]
ACCESS_TOKEN = your_token
UID = your_uid 
填完之後，好沒問題來！
我們來拿 UID！

把這支程式跑起來：
python TelegramBot


如果一切沒問題，你的終端機會顯示：

apscheduler.scheduler - INFO - Scheduler started


再開 Telegram 到你與這隻機器人的對話框，輸入：
/getUID這樣在 Telegram 對話框 及 終端機應該都會把你的 UID 噴出來，
把 UID 回填到 config.ini 裡面去。

然後把這支程式關掉（Ctrl-C）


在你想監聽的 Python 程式最上面加入：
from TelegramBot import Alert


程式執行完處加入：
Alert()


把機器人跑起來，把你想監聽的程式也跑起來。

當程式執行完時便會出現：







已解決！
