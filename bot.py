import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from slang_dict import SLANG_DICT

TOKEN = "8400446821:AAHCNAPs91AvETn1tUe6jr8oU3NdZBzaNu4"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я бот-словарь современного русского сленга.\n\n"
        "Отправь мне сленговое слово, и я объясню его значение."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    if text in SLANG_DICT:
        item = SLANG_DICT[text]
        await update.message.reply_text(
            f"📘 Слово: {text}\n"
            f"📝 Значение: {item['meaning']}\n"
            f"💬 Пример: {item['example']}"
        )
    else:
        await update.message.reply_text(
            "❌ Такого слова пока нет в моём словаре.\n"
            "Попробуйте другое сленговое слово."
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()