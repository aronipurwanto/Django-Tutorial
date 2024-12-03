from django.urls import re_path

from pos import views

urlpatterns = [
    re_path(r'^$', views.categoryList()),
]