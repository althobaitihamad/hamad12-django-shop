from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """تصنيفات المنتجات"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("اسم التصنيف")
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("وصف التصنيف")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإضافة")
    )

    class Meta:
        verbose_name = _("تصنيف")
        verbose_name_plural = _("التصنيفات")
        ordering = ['-created_at']

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    """تفاصيل المنتجات"""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_("التصنيف")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("اسم المنتج")
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("وصف المنتج")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("السعر (بالريال)")
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_("الكمية المتاحة")
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name=_("صورة رئيسية للمنتج")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإضافة")
    )

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ['-created_at']

    def __str__(self):
        return str(self.name)


class ProductImage(models.Model):
    """الصور الإضافية الخاصة بكل منتج"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("المنتج")
    )
    image = models.ImageField(
        upload_to='products/gallery/',
        verbose_name=_("الصورة الإضافية")
    )
    caption = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_("وصف الصورة (اختياري)")
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الرفع")
    )

    class Meta:
        verbose_name = _("صورة المنتج")
        verbose_name_plural = _("معرض الصور الإضافية")
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"📸 {self.product.name}"

    def image_preview(self):
        """عرض مصغّر للصورة في لوحة التحكم"""
        from django.utils.html import mark_safe
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="80" style="border-radius:8px;" />')
        return _("لا توجد صورة")
    image_preview.short_description = _("معاينة الصورة")
