from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product

def product_list(request):
    categories = Category.objects.all()
    first_category = categories.first()  # گرفتن اولین دسته‌بندی
    products = Product.objects.filter(category=first_category) if first_category else []
    return render(request, 'index.html', {'categories': categories, 'products': products})

def get_products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    data = [{'name': product.name, 'price': str(product.price)} for product in products]
    return JsonResponse({'products': data})
