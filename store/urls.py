from django.urls import path
from . import views

# =======================================
# 🛍️ مسارات تطبيق المتجر (store)
# =======================================
urlpatterns = [
    # 🏠 صفحة جميع المنتجات
    path('products/', views.products_view, name='products'),
]
