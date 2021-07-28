import os
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@bot.on_message(filters.command(['start']))
def start(client, message):
    message.reply(f"Hello {message.from_user.first_name} how are you",
    reply_markup = InlinekeyboardMarkup([[InlineKeyboardButton("Owner", url = "t.me/xxxtentacion_OF_TG")]]))

bot.run()


