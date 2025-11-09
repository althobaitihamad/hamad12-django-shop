from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """الملف الشخصي للمستخدم"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="المدينة")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ContactMessage(models.Model):
    """نموذج مراسلة المستخدمين"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"رسالة من {self.name}"
