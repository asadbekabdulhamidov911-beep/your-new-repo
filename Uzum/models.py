# Uzum/models.py
from django.db import models
from django.contrib.auth.models import User

# ============ SIZNING MAVJUD MODELLARINGIZ ============

class Category(models.Model):
    nomi = models.CharField(max_length=100)
    rasmi = models.ImageField(upload_to='category/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.nomi

class Product(models.Model):
    kategoriya = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='mahsulotlar', null=True, blank=True)
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=50)
    narxi = models.IntegerField()
    skidka = models.IntegerField()
    rate = models.FloatField(null=True)
    is_aksiya = models.BooleanField(default=False)
    is_arzonlashdi = models.BooleanField(default=False)
    tavsif = models.TextField(null=True)
    
    def __str__(self):
        return self.nomi

# ============ TELEGRAM USER MODELI (QO'SHILDI) ============

class TelegramUser(models.Model):
    """Telegram foydalanuvchilari modeli"""
    chat_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'telegram_users'
        verbose_name = "Telegram foydalanuvchisi"
        verbose_name_plural = "Telegram foydalanuvchilari"
    
    def __str__(self):
        return f"{self.username or self.chat_id}"