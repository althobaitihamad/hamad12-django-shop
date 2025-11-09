from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from store.models import Product


class Cart(models.Model):
    """عربة التسوق"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name=_("المستخدم")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإنشاء")
    )

    class Meta:
        verbose_name = _("عربة تسوق")
        verbose_name_plural = _("عربات التسوق")
        ordering = ['-created_at']

    def __str__(self):
        return f"🛒 عربة {self.user.username}"


class CartItem(models.Model):
    """عنصر داخل عربة التسوق"""
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_("عربة التسوق")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("المنتج")
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("الكمية")
    )

    class Meta:
        verbose_name = _("عنصر عربة")
        verbose_name_plural = _("عناصر عربات التسوق")

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    def total_price(self):
        return self.quantity * self.product.price
    total_price.short_description = _("الإجمالي")


class Order(models.Model):
    """الطلب بعد تأكيد الشراء"""

    class OrderStatus(models.TextChoices):
        PENDING = 'pending', _("قيد المعالجة")
        PROCESSING = 'processing', _("قيد التنفيذ")
        COMPLETED = 'completed', _("مكتمل")
        CANCELLED = 'cancelled', _("ملغي")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("المستخدم")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الطلب")
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("إجمالي السعر")
    )
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name=_("حالة الطلب")
    )

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"


class OrderItem(models.Model):
    """تفاصيل المنتجات داخل الطلب"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_("الطلب")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("المنتج")
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("الكمية")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("السعر للوحدة")
    )

    class Meta:
        verbose_name = _("عنصر طلب")
        verbose_name_plural = _("عناصر الطلبات")

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    def subtotal(self):
        return self.price * self.quantity
    subtotal.short_description = _("الإجمالي الجزئي")


class Payment(models.Model):
    """نموذج الدفع"""
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='payment',
        verbose_name=_("الطلب")
    )
    method = models.CharField(
        max_length=50,
        verbose_name=_("طريقة الدفع")
    )
    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("رقم العملية")
    )
    paid = models.BooleanField(
        default=False,
        verbose_name=_("تم الدفع؟")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الدفع")
    )

    class Meta:
        verbose_name = _("دفعة")
        verbose_name_plural = _("المدفوعات")
        ordering = ['-created_at']

    def __str__(self):
        return f"💰 دفع الطلب رقم {self.order.id}"
