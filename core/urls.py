from django.urls import path
from . import views

# ==============================
# 🌐 روابط تطبيق core
# ==============================
urlpatterns = [
    # 🏠 الصفحة الرئيسية
    path('', views.home, name='home'),

    # 🟢 إنشاء حساب جديد
    path('register/', views.register_view, name='register'),

    # 🔵 تسجيل الدخول
    path('login/', views.login_view, name='login'),
]
