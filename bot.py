import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8916405958:AAFizipiIHZQAPRQfMBL94GgyoMEQM-3zCU"
GAME_SHORT_NAME = "my_horse"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً بك في لعبة سباق الخيول! اضغط على زر اللعب أدناه للاستمتاع باللعبة.")
    await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=GAME_SHORT_NAME)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    print("البوت يعمل الآن...")
    application.run_polling()
  
