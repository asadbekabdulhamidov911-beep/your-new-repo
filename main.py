import os
import django
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from authentication.models import TelegramUser

BOT_TOKEN = "8808790681:AAHcWMFbwLfuVTQ4N6QI8Tv7DpRHnJDcFjs"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    TelegramUser.objects.get_or_create(
        chat_id=message.chat.id,
        defaults={'username': message.from_user.username or ""}
    )
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("foydalanuvchilarni ko'rish"))
    bot.send_message(message.chat.id, "Kerakli bo'limni tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "foydalanuvchilarni ko'rish")
def show_all_users(message):
    users = User.objects.all()
    text = "Ro'yxatdan o'tgan foydalanuvchilar:\n\n"
    for user in users:
        text += f"User: {user.username} | Email: {user.email}\n"
    
    bot.send_message(message.chat.id, text)

if __name__ == '__main__':
    bot.polling(none_stop=True)