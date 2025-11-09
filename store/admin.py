from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    """عرض الصور الإضافية داخل صفحة المنتج"""
    model = ProductImage
    extra = 1
    verbose_name = "صورة إضافية"
    verbose_name_plural = "الصور الإضافية"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """إدارة التصنيفات في لوحة التحكم"""
    list_display = ('name', 'description', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        ('بيانات التصنيف', {
            'fields': ('name', 'description')
        }),
        ('معلومات إضافية', {
            'fields': ('created_at',),
        }),
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """إدارة المنتجات في لوحة التحكم"""
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_display_links = ('name',)
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'category__name')
    inlines = [ProductImageInline]
    ordering = ('-created_at',)
    fieldsets = (
        ('بيانات المنتج', {
            'fields': ('name', 'category', 'description', 'price', 'stock', 'image')
        }),
        ('معلومات إضافية', {
            'fields': ('created_at',),
        }),
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
