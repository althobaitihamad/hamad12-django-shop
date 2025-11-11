from django.shortcuts import render

# 🏬 عرض صفحة المنتجات
def products_view(request):
    """عرض صفحة جميع المنتجات"""
    return render(request, 'store_templates/products.html')
