from django.contrib import admin
from django.urls import re_path

from . import views
from blog import views as blogViews
from about import views as aboutViews

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^blog/$', blogViews.index),
    re_path(r'^about/$', aboutViews.index),
    re_path(r'^$', views.index),
]
