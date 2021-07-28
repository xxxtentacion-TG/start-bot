import os
from program import client as bot
from program import Filters
from program.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@bot.on_message(filters.command(['start']))
def start(client, message)
    message.reply(f"Hello {message.from_user.first_name} how are you",
    reply_markup = InlinekeyboardMarkup([[InlineKeyboardButton("Owner", url = "t.me/xxxtentacion_OF_TG")]]))

bot.run()