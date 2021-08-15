from telegram.ext import Updater,CommandHandler,CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from telegram.update import Update
import local_settings
import requests


updater = Updater(token=local_settings.TELEGRAM_TOKEN)

def start(update:Update, context:CallbackContext):
    update.message.reply_text("Short instruction on how to use our bot. Write command like /search helicopter. ")
   

def search(update:Update, context:CallbackContext):
    args = context.args

    if len(args) == 0:
        update.message.reply_text("Please write something otherwise we cannot help you.")
    else:    
        searched_text = ' '.join(args)
        response = requests.get("https://en.wikipedia.org/w/api.php", {
            "action": "opensearch",
            "search": searched_text,
            "namespace": 0,
            "limit": 1,
            "format": "json",
        })
        link = response.json()[3]

        if len(link):
            update.message.reply_text("This is searched result: " + link[0])
        else:
            update.message.reply_text("We could't find anything")
        

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()


