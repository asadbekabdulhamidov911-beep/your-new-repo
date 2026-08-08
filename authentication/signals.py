from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import TelegramUser
import telebot

BOT_TOKEN = "8808790681:AAHcWMFbwLfuVTQ4N6QI8Tv7DpRHnJDcFjs"

@receiver(post_save, sender=User)
def notify_all_telegram_users(sender, instance, created, **kwargs):
    if created:
        try:
            bot = telebot.TeleBot(BOT_TOKEN)
            telegram_users = TelegramUser.objects.all()
            text = f"Yangi foydalanuvchi ro'yxatdan o'tdi:\n\nUsername: {instance.username}\nEmail: {instance.email}"
            
            for tg_user in telegram_users:
                try:
                    bot.send_message(tg_user.chat_id, text)
                except Exception:
                    pass
        except Exception as e:
            print(f"Telegram bildirishnomada xatolik: {e}")