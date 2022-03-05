from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import commands as c
import my_bot_api



updater = Updater(my_bot_api.api)
print("Server started")

updater.dispatcher.add_handler(CommandHandler('start', c.help))
updater.dispatcher.add_handler(CommandHandler('help', c.help))
updater.dispatcher.add_handler(CommandHandler('stats', c.stats))
updater.dispatcher.add_handler(CommandHandler('cheat', c.cheat))
updater.dispatcher.add_handler(MessageHandler(Filters.text, c.turn))

updater.start_polling()
updater.idle()