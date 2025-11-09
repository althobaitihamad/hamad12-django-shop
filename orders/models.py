from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Cart(models.Model):
    """عربة التسوق"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"عربة {self.user.username}"


class CartItem(models.Model):
    """عنصر داخل عربة التسوق"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    def total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    """الطلب بعد تأكيد الشراء"""
    STATUS_CHOICES = [
        ('pending', 'قيد المعالجة'),
        ('processing', 'قيد التنفيذ'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"طلب {self.id} - {self.user.username}"


class OrderItem(models.Model):
    """تفاصيل المنتجات داخل الطلب"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"


class Payment(models.Model):
    """نموذج الدفع"""
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    method = models.CharField(max_length=50, verbose_name="طريقة الدفع")
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"دفع طلب {self.order.id}"
