import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product



def get_hot_product():
    products = Product.objects.all()
    return random.choice(products)


def get_same_products(product):
    return Product.objects.filter(
        category=product.category).exclude(pk=product.pk)


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    hot_product = get_hot_product()

    context = {
        'page_title': 'каталог',
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
    }
    return render(request, 'mainapp/products.html', context)


def category_items(request, category_pk, page_num=1):
    if category_pk == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=category_pk)

    products_paginator = Paginator(products, 2)
    try:
        products = products_paginator.page(page_num)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        'page_title': 'каталог',
        'products': products,
        'category_pk': category_pk,
    }
    return render(request, 'mainapp/category_items.html', context)


def product_page(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    context = {
        'page_title': 'продукт',
        'product': product,
        'category_pk': product.category_id,
    }
    return render(request, 'mainapp/product_page.html', context)


def contact(request):
    _locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Краснодар',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
    ]

    context = {
        'page_title': 'контакты',
        'locations': _locations,
    }
    return render(request, 'mainapp/contact.html', context)
