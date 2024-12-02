from django.urls import re_path

from . import views

urlpatterns = [
	re_path(r'^recent/$',views.recent),
	re_path(r'^$', views.index),
]