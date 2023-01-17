from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.products, name='products'),
    path('category/<int:category_pk>/', mainapp.category_items, name='category_items'),  # category_pk -> int
    # re_path(r'category/(?P<category_pk>\d+)/', mainapp.category_items, name='category_items'),  # category_pk -> str

    path('product/<int:product_pk>/', mainapp.product_page, name='product_page'),

    path('contact/', mainapp.contact, name='contact'),
]
