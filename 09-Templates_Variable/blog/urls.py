from django.urls import re_path

from . import views

urlpatterns = [
	re_path(r'^cerita/$',views.cerita),
	re_path(r'^news/$',views.news),
	re_path(r'^$', views.index),
]