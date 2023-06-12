import os

from dotenv import load_dotenv
from model.csv_parser import parse_file, create_generator
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()
generator = None


def create_the_generator():
    weapons = parse_file("../assets/items.csv")
    slots = parse_file("../assets/slots.csv")

    return create_generator("../assets/modifications.csv", weapons, slots)


# noinspection PyUnresolvedReferences
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    generator.generate_random_class()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(generator), parse_mode="Markdown")
    generator.clear()


def main():
    global generator
    generator = create_the_generator()
    bot_token = os.getenv('BOT_TOKEN')
    application = ApplicationBuilder().token(bot_token).build()

    generate_handler = CommandHandler('generate', generate)
    application.add_handler(generate_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
