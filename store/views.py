from django.shortcuts import render,get_object_or_404
from .models import product
from category.models import Category

def store(request,category_slug = None):
    categories = None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = product.objects.filter(category = categories, is_avilable = True)
        product_count = products.count()
    else:
        products = product.objects.all().filter( is_avilable =True)
        product_count = products.count()
    data = {
        'products':products,
        'product_count':product_count
    }
    return render(request,'store/store.html',data)

def product_detail(request, category_slug, product_slug):
    try:
        single_products = product.objects.get (category__slug=category_slug, slug = product_slug)
    except Exception as e:
        raise e
    context = {
        'single_products':single_products,
    }

    return render(request,'store/product_detail.html',context)
