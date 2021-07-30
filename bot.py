import os
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message

bot = Client('mybot',
      bot_token="1853498659:AAFdnSWzBEA4wqp8qpnViDKyvOSjV4y9-vU",
      api_id=3020564,
      api_hash="91c026fadfdc442f504a0bd3e5c8cd18",
      )

@bot.on_message(filters.command(['start']))
def start(client, message):
    message.reply(f"Hello {message.from_user.first_name} how are you",
    reply_markup = InlineKeyboardMarkup(
      [
         [
            InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG'),
            InlineKeyboardButton('GROUP', url='https://t.me/MGMOVIEGRAM')
         ],
         [
            InlineKeyboardButton('GROUP', url='https://t.me/MGMOVIEGRAM')
         ]
      ]
      )
     )
@bot.on_message(filters.command(['help']))
def help(client, message):
    await bot.send_photo(
      photo="https://telegra.ph/file/e7a6d96ab0961d60f75a0.jpg",
      caption=f"{message.from_user.first_name} What you Want",
      reply_markup = InlineKeyboardMarkup(
    [
         [
            InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG'),
            InlineKeyboardButton('GROUP', url='https://t.me/MGMOVIEGRAM')
         ],
         [
            InlineKeyboardButton('GROUP', url='https://t.me/MGMOVIEGRAM')
         ]
      ]
      )
     )


bot.run()


