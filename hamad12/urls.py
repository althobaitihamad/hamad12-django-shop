from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ===========================
# روابط المشروع الأساسية
# ===========================
urlpatterns = [
    # لوحة التحكم (Admin Panel)
    path('admin/', admin.site.urls),

    # ===========================
    # روابط التطبيقات الداخلية
    # ===========================
    path('', include('core.urls')),          # التطبيق الأساسي (الصفحة الرئيسية)
    path('store/', include('store.urls')),   # تطبيق المتجر
    path('orders/', include('orders.urls')), # تطبيق الطلبات
]

# ===========================
# عرض الملفات الثابتة والإعلامية أثناء التطوير
# ===========================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
