from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, Payment


class CartItemInline(admin.TabularInline):
    """لعرض محتوى العربة مباشرة من صفحة العربة"""
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    inlines = [CartItemInline]
    ordering = ('-created_at',)


class OrderItemInline(admin.TabularInline):
    """لعرض تفاصيل الطلب من صفحة الطلب"""
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]
    ordering = ('-created_at',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'method', 'paid', 'created_at')
    list_filter = ('paid', 'method')
    search_fields = ('order__id', 'transaction_id')
    ordering = ('-created_at',)
