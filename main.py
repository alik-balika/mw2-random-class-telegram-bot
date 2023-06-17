import os

from dotenv import load_dotenv
from model.csv_parser import parse_file, create_generator
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()
generator = None
NUM_ARGUMENTS = 2


def create_the_generator():
    weapons = parse_file("../assets/items.csv")
    slots = parse_file("../assets/slots.csv")

    return create_generator("../assets/modifications.csv", weapons, slots)


# noinspection PyUnresolvedReferences
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(get_user_name(update) + " generated a random class")
    num_attachments, is_overkill_on = parse_args(context.args)

    generator.generate_random_class(num_attachments, is_overkill_on)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(generator), parse_mode="Markdown")
    generator.clear()


def get_user_name(update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
        if user.last_name:
            name += " " + user.last_name
        if user.username:
            name += " (@" + user.username + ")"
        return name
    else:
        return "Unknown User"


def parse_args(args):
    is_overkill_on, num_attachments = iterate_over_args_and_assign_to_values(args)

    return num_attachments, is_overkill_on


def iterate_over_args_and_assign_to_values(args):
    num_attachments = None
    is_overkill_on = None
    for i in range(min(NUM_ARGUMENTS, len(args))):
        arg = args[i]
        if is_valid_number_of_attachments(arg):
            num_attachments = int(arg)
        elif arg.lower() in ['yes', 'true', 'y']:
            is_overkill_on = True
    return is_overkill_on, num_attachments


def is_valid_number_of_attachments(num_attachments):
    return num_attachments.isdigit() and 0 <= int(num_attachments) <= 5


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = '''\
    This bot supports the following commands:
    
    */generate* - Generate a random class with attachments and overkill.

The */generate* command accepts the following arguments (in any order):
    - *num_attachments*: Specifies the desired number of attachments (an integer between 0 and 5, inclusive).
    - *overkill*: Specifies if overkill should always be on. Valid values: 'yes', 'true', 'y'.

Examples:
    - */generate* - Generate a class with random number of attachments and random overkill.
    - */generate 3* - Generate a class with 3 attachments and random overkill.
    - */generate yes* - Generate a class with random number of attachments and overkill always on.
    - */generate yes 2* - Generate a class with 2 attachments and overkill always on.

Note: If no arguments or invalid arguments are provided, the bot will use default values for attachments and overkill.

Feel free to experiment and customize your class generation!
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text, parse_mode="Markdown")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {user.first_name}! Welcome to the "
                                                                          f"bot. Use /help to see the available "
                                                                          f"commands.")


def main():
    global generator
    generator = create_the_generator()
    bot_token = os.getenv('BOT_TOKEN')
    application = ApplicationBuilder().token(bot_token).build()

    generate_handler = CommandHandler('generate', generate)
    help_handler = CommandHandler('help', help_command)
    start_handler = CommandHandler('start', start)
    application.add_handler(generate_handler)
    application.add_handler(help_handler)
    application.add_handler(start_handler)

    application.run_polling()


if __name__ == '__main__':
    print("Bot has started running")
    main()
