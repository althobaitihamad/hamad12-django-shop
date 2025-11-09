from django.contrib import admin
from django.utils.html import format_html
from .models import Cart, CartItem, Order, OrderItem, Payment


# 🛒 العناصر داخل العربة
class CartItemInline(admin.TabularInline):
    """لعرض محتوى العربة مباشرة من صفحة العربة"""
    model = CartItem
    extra = 1
    verbose_name = "عنصر في العربة"
    verbose_name_plural = "عناصر العربة"
    readonly_fields = ("total_price_display",)

    def total_price_display(self, obj):
        """عرض السعر الإجمالي لكل عنصر"""
        return f"{obj.total_price():,.2f} ريال" if obj.product else "-"
    total_price_display.short_description = "الإجمالي"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """إدارة عربات التسوق"""
    list_display = ("user", "created_at")
    list_display_links = ("user",)
    inlines = [CartItemInline]
    ordering = ("-created_at",)
    search_fields = ("user__username",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("🛍️ بيانات العربة", {
            "fields": ("user",),
            "description": "معلومات أساسية عن العربة والمستخدم المرتبطة به"
        }),
        ("⏱️ معلومات إضافية", {
            "fields": ("created_at",),
        }),
    )

    class Meta:
        verbose_name = "عربة تسوق"
        verbose_name_plural = "عربات التسوق"


# 📦 العناصر داخل الطلب
class OrderItemInline(admin.TabularInline):
    """لعرض تفاصيل المنتجات داخل الطلب"""
    model = OrderItem
    extra = 1
    verbose_name = "عنصر في الطلب"
    verbose_name_plural = "عناصر الطلب"
    readonly_fields = ("subtotal_display",)

    def subtotal_display(self, obj):
        """عرض الإجمالي الجزئي"""
        return f"{obj.subtotal():,.2f} ريال" if obj.product else "-"
    subtotal_display.short_description = "الإجمالي الجزئي"


# 💸 الدفعات
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """إدارة المدفوعات"""
    list_display = ("order", "method", "paid_status", "created_at")
    list_filter = ("paid", "method")
    search_fields = ("order__id", "transaction_id", "method")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    def paid_status(self, obj):
        """عرض حالة الدفع بألوان"""
        color = "green" if obj.paid else "red"
        text = "✅ مدفوع" if obj.paid else "❌ لم يُدفع"
        return format_html(f'<span style="color:{color}; font-weight:bold;">{text}</span>')
    paid_status.short_description = "حالة الدفع"

    class Meta:
        verbose_name = "دفعة"
        verbose_name_plural = "المدفوعات"


# 📋 الطلبات
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """إدارة الطلبات"""
    list_display = ("id", "user", "status_colored", "total_price_display", "created_at")
    list_display_links = ("id", "user")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "id")
    inlines = [OrderItemInline]
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("📦 بيانات الطلب", {
            "fields": ("user", "status", "total_price"),
            "description": "تفاصيل عامة حول الطلب"
        }),
        ("⏱️ معلومات إضافية", {
            "fields": ("created_at",),
            "description": "تاريخ إنشاء الطلب"
        }),
    )

    def total_price_display(self, obj):
        """عرض الإجمالي بصيغة منسقة"""
        return f"{obj.total_price:,.2f} ريال"
    total_price_display.short_description = "إجمالي السعر"

    def status_colored(self, obj):
        """عرض الحالة بألوان مميزة"""
        colors = {
            "pending": "orange",
            "processing": "blue",
            "completed": "green",
            "cancelled": "red",
        }
        color = colors.get(obj.status, "black")
        label = dict(obj.OrderStatus.choices).get(obj.status, obj.status)
        return format_html(f'<b style="color:{color};">{label}</b>')
    status_colored.short_description = "حالة الطلب"

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"
