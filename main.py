from threading import local
from telegram.bot import Bot
from telegram.user import User  
from telegram.ext import Updater,Dispatcher,CommandHandler,CallbackContext
from telegram.update import Update
from settings import local_settings


# bot =  Bot(token="1912334379:AAF9Xdi9y3hAebzqpyCQc01SalrFqXC4MCU")
# user : User = bot.get_me()   # it wraps to the User class.
# print(user.link)   # it generates bot link 

updater = Updater(token=local_settings.TELEGRAM_TOKEN)

def start(update:Update, context:CallbackContext):
    update.message.reply_text("Hello Muzaffarbek")
    context.bot.send_message(chat_id=update.message.chat_id,text="OOPS")
    print(update)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()


