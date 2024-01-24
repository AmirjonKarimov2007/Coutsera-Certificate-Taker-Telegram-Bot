from django.contrib import admin
from .models import Certificate,User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['id','full_name', 'username', 'telegram_id', 'created_at']
    search_fields = ['id','full_name', 'username','telegram_id']
@admin.register(Certificate)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism_familiya', 'telegram_id', 'phone_number', 'email', 'password', 'certificate_link', 'chek','created_at','updated_at']
