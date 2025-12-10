from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Bot working!")

updater = Updater("YOUR_TOKEN", use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()