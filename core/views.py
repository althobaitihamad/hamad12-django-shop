from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from store.models import Product  # ✅ استدعاء المنتجات لعرضها في الصفحة الرئيسية
from .models import UserProfile


# ============================================================
# 🏠 الصفحة الرئيسية
# ============================================================
def home(request):
    """عرض الصفحة الرئيسية مع قائمة المنتجات"""
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)


# ============================================================
# 🟢 إنشاء حساب جديد
# ============================================================
def register_view(request):
    """صفحة إنشاء حساب جديد"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # ✅ التحقق من اكتمال الحقول
        if not username or not email or not password or not confirm_password:
            messages.error(request, "⚠️ يرجى تعبئة جميع الحقول المطلوبة.")
            return redirect('register')

        # ❌ التحقق من تطابق كلمات المرور
        if password != confirm_password:
            messages.error(request, "❌ كلمتا المرور غير متطابقتان.")
            return redirect('register')

        # ⚠️ التحقق من وجود المستخدم مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ اسم المستخدم مستخدم مسبقًا.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "⚠️ البريد الإلكتروني مستخدم مسبقًا.")
            return redirect('register')

        # 🧩 إنشاء المستخدم وربط الملف الشخصي
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user)
            messages.success(request, "✅ تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"حدث خطأ أثناء إنشاء الحساب: {e}")
            return redirect('register')

    return render(request, 'core_templates/register.html')


# ============================================================
# 🔵 تسجيل الدخول
# ============================================================
def login_view(request):
    """صفحة تسجيل الدخول"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"👋 مرحبًا {username}!")
            return redirect('home')
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة.")

    return render(request, 'core_templates/login.html')


# ============================================================
# 🔴 تسجيل الخروج
# ============================================================
def logout_view(request):
    """تسجيل خروج المستخدم"""
    logout(request)
    messages.info(request, "👋 تم تسجيل الخروج بنجاح.")
    return redirect('home')
