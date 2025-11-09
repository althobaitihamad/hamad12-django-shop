from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # ===========================
    # روابط التطبيقات الداخلية
    # ===========================
    path('', include('core.urls')),          # التطبيق الأساسي (الصفحة الرئيسية)
    path('store/', include('store.urls')),   # تطبيق المتجر
    path('orders/', include('orders.urls')), # تطبيق الطلبات
]
