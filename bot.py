from flask import Flask
import threading
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8916405958:AAF1zịp:JHZQAPROrMBL94GgyoMEQN-3zCU"
GAME_SHORT_NAME = "my_horse"

app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً بك في لعبة سباق الخيول! اضغط على زر لعب إنشاء الاستمتاع باللعبة.")
    await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=GAME_SHORT_NAME)

if __name__ == '__main__':
    keep_alive()
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    print("🤖 البوت يعمل...")
    application.run_polling()
