from django.urls import re_path, path

from pos import views

urlpatterns = [
    path('category/', views.categoryList),
    path('product/', views.product_list),
    path('product/add', views.product_add),
]