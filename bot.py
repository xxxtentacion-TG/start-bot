import os #your choice 
from pyrogram import Client, filters #important 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery # for buttons

bot = Client('test_bot', # your choice | # to run a code its important 
      bot_token="1853498659:AAFdnSWzBEA4wqp8qpnViDKyvOSjV4y9-vU", #bot token
      api_id=3020564, # app id
      api_hash="91c026fadfdc442f504a0bd3e5c8cd18", # api hash 
      )

@bot.on_message(filters.command(['start'])) # commmand
def start(client, message): 
    message.reply(f"Hello {message.from_user.first_name} how are you", #reply message 
    reply_markup = InlineKeyboardMarkup( # button
      [
         [
            InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG'),
            InlineKeyboardButton('group', url='https://t.me/MGMOVIEGRAM')
         ],
         [
            InlineKeyboardButton('help', callback_data="help"),
         ]
      ]
      )
     )
@bot.on_message(filters.command(['help']))
def help(client, message):
    message.reply(f"{message.from_user.first_name} What you Want",
    reply_markup = InlineKeyboardMarkup(
    [
         [
            InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG'),
            InlineKeyboardButton('group', url='https://t.me/MGMOVIEGRAM')
         ],
         [
            InlineKeyboardButton('home', callback_data='start'),
            InlineKeyboardButton('help', callback_data="help"),
         ]
      ]
      )
     )
@bot.on_message(filters.command(['about']))
def about(client, message):
    message.reply(f"{message.from_user.first_name} What you Want",
    reply_markup = InlineKeyboardMarkup(
    [
         [
            InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG'),
            InlineKeyboardButton('group', url='https://t.me/MGMOVIEGRAM')
         ]
         [
            InlineKeyboardButton('home', callback_data='start'),
            InlineKeyboardButton('help', callback_data="help"),
         ]
      ]
      )
     )
#➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️
@bot.on_callback_query()
def common(client, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    user_name = query.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    if data == "start":
        query.message.edit(f"your start message.",
        reply_markup = InlineKeyboardMarkup(  
        [
           [
              InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG')
           ]
         ]
       ))

    if data == "help":
        query.message.edit(f"your help message.",
        reply_markup = InlineKeyboardMarkup(  
        [
           [
              InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG')
           ]
         ]
       ))

    if data == "about":
        query.message.edit(f"your about message.",
        reply_markup = InlineKeyboardMarkup(  
        [
           [
              InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG')
           ]
         ]
       ))
#➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️
   

bot.run() # to run a code its important 


