from django.db import models

class TelegramUser(models.Model):
    telegram_username = models.CharField(max_length=150, unique=True)
    telegram_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_username