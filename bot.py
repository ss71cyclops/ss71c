from telegram.ext import Updater, CommandHandler

import os

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Команда /start
def start(update, context):
    update.message.reply_text("Привет, я апашка!")
    update.message.reply_text("Хочешь узнать мой секрет?", reply_markup={
        "keyboard": [[{"text": "Да"}]],
        "resize_keyboard": True,
        "one_time_keyboard": True
    })

# Обработка ответа
def handle_message(update, context):
    if update.message.text.lower() == "да":
        for _ in range(50):
            update.message.reply_text("".join(["%$@"[i % 3] for i in range(10)]))
        for _ in range(10):
            update.message.reply_text("===X7A V1G===")
        for _ in range(40):
            update.message.reply_text("".join(["@*&"[i % 3] for i in range(10)]))

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("message", handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
