from django.urls import re_path

from pos import views

urlpatterns = [
    re_path(r'^category/', views.categoryList),
    re_path(r'^product/', views.product_list),
    re_path(r'^product/add', views.product_add),
]