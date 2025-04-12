import telebot
from telebot import types

BOT_TOKEN = "8004861258:AAHmwO5OD8fLtyeWD6IL9TBoOLuIXP3zL48"
ADMIN_IDS = [635874172]  # Admin Telegram ID'lar

bot = telebot.TeleBot(BOT_TOKEN)
auto_replies = {
    "salom": "Salom, guruhimizga xush kelibsiz!",
    "qalesiz": "Yaxshi, sizni-chi?"
}

@bot.message_handler(commands=["start", "help"])
def start_handler(message):
    bot.reply_to(message, "Assalomu alaykum! Men guruhni tozalovchi botman.")

@bot.message_handler(content_types=["new_chat_members", "left_chat_member"])
def handle_join_leave(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

@bot.message_handler(commands=["panel"])
def panel_handler(message):
    if message.from_user.id in ADMIN_IDS:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("Auto Replies", "Guruh Tozalash")
        bot.send_message(message.chat.id, "Admin Panel", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text in auto_replies.keys())
def auto_reply_handler(message):
    bot.reply_to(message, auto_replies[message.text.lower()])

@bot.message_handler(func=lambda msg: True)
def fallback_handler(message):
    pass

bot.polling()
