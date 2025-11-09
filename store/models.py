from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """تصنيفات المنتجات"""
    name = models.CharField(max_length=100, unique=True, verbose_name=_("اسم التصنيف"))
    description = models.TextField(blank=True, null=True, verbose_name=_("الوصف"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإضافة"))

    class Meta:
        verbose_name = _("تصنيف")
        verbose_name_plural = _("التصنيفات")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Product(models.Model):
    """تفاصيل المنتجات"""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_("التصنيف"),
    )
    name = models.CharField(max_length=150, verbose_name=_("اسم المنتج"))
    description = models.TextField(blank=True, null=True, verbose_name=_("الوصف"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("السعر"))
    stock = models.PositiveIntegerField(default=0, verbose_name=_("الكمية المتاحة"))
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name=_("صورة المنتج"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإضافة"))

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """صور إضافية لكل منتج"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("المنتج"),
    )
    image = models.ImageField(upload_to='products/gallery/', verbose_name=_("الصورة"))
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الرفع"))

    class Meta:
        verbose_name = _("صورة المنتج")
        verbose_name_plural = _("معرض الصور")

    def __str__(self):
        return f"صورة - {self.product.name}"
