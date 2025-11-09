from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    """الملف الشخصي للمستخدم"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_("المستخدم")
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_("رقم الجوال")
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("العنوان")
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("المدينة")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإنشاء")
    )

    class Meta:
        verbose_name = _("ملف المستخدم")
        verbose_name_plural = _("ملفات المستخدمين")
        ordering = ['-created_at']

    def __str__(self):
        return f"👤 {self.user.username}"


class ContactMessage(models.Model):
    """نموذج مراسلة المستخدمين"""
    name = models.CharField(
        max_length=100,
        verbose_name=_("الاسم")
    )
    email = models.EmailField(
        verbose_name=_("البريد الإلكتروني")
    )
    subject = models.CharField(
        max_length=150,
        verbose_name=_("عنوان الرسالة")
    )
    message = models.TextField(
        verbose_name=_("نص الرسالة")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإرسال")
    )

    class Meta:
        verbose_name = _("رسالة تواصل")
        verbose_name_plural = _("رسائل التواصل")
        ordering = ['-created_at']

    def __str__(self):
        return f"✉️ رسالة من {self.name}"
