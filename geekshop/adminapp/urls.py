from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # ShopUser
    path('', adminapp.ShopUserList.as_view(), name='index'),
    path('user/create/', adminapp.ShopUserCreateView.as_view(), name='user_create'),
    path('user/update/<int:user_pk>/', adminapp.ShopUserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:user_pk>/', adminapp.ShopUserDeleteView.as_view(), name='user_delete'),

    # ProductCategory
    path('categories/', adminapp.categories, name='categories'),
    path('category/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/products/', adminapp.category_products, name='category_products'),
    path('product/<int:pk>/', adminapp.ProductDetail.as_view(), name='product_detail'),
    path('category/<int:pk>/product/create/', adminapp.product_create, name='product_create'),
]
