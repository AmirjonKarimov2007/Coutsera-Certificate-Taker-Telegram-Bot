from django.db import models
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name='Fullname', max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram_id', unique=True, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.full_name
class Certificate(models.Model):
    id = models.BigAutoField(primary_key=True)
    telegram_id = models.BigIntegerField(null=False)
    ism_familiya = models.CharField(max_length=255, null=True)
    phone_number = models.BigIntegerField(null=True)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    certificate_link = models.CharField(max_length=255, null=True)
    chek = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"Certificate {self.id}"
