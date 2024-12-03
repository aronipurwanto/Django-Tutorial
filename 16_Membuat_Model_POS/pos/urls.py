from django.urls import re_path, path

from pos import views

urlpatterns = [
    path('category/', views.categoryList, name='categoryList'),
    path('product/', views.product_list, name='productList'),
    path('product/add', views.product_add, name='product_add'),
]