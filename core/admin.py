from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile, ContactMessage


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """إدارة ملفات المستخدمين في لوحة التحكم"""
    list_display = ('user', 'phone_display', 'city', 'created_at')
    search_fields = ('user__username', 'phone', 'city')
    list_filter = ('city', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ('👤 بيانات المستخدم', {
            'fields': ('user', 'phone', 'city', 'address'),
            'description': 'المعلومات الشخصية للمستخدم'
        }),
        ('⏱️ معلومات إضافية', {
            'fields': ('created_at',),
            'description': 'تاريخ إنشاء الملف الشخصي'
        }),
    )

    def phone_display(self, obj):
        """عرض رقم الجوال أو إشعار عند عدم وجوده"""
        if obj.phone:
            return obj.phone
        return format_html('<span style="color:#999;">غير متوفر</span>')
    phone_display.short_description = "رقم الجوال"

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """إدارة رسائل التواصل في لوحة التحكم"""
    list_display = ('name', 'email_link', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ('📩 تفاصيل المرسل', {
            'fields': ('name', 'email'),
            'description': 'بيانات الشخص الذي أرسل الرسالة'
        }),
        ('📝 محتوى الرسالة', {
            'fields': ('subject', 'message'),
            'description': 'تفاصيل الرسالة المرسلة من المستخدم'
        }),
        ('⏱️ معلومات إضافية', {
            'fields': ('created_at',),
            'description': 'تاريخ إرسال الرسالة'
        }),
    )

    def email_link(self, obj):
        """عرض البريد الإلكتروني كرابط"""
        return format_html(f'<a href="mailto:{obj.email}">{obj.email}</a>')
    email_link.short_description = "البريد الإلكتروني"

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"
