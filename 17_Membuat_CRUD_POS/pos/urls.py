from django.urls import re_path, path

from pos import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:pk>/update/', views.update_product, name='update_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:pk>/update/', views.update_category, name='update_category'),
    path('categories/<int:pk>/delete/', views.delete_category, name='delete_category'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/<int:pk>/update/', views.update_customer, name='update_customer'),
    path('customers/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
]