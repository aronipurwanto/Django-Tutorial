from django.urls import re_path,include
from django.contrib import admin

from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^about/', include('about.urls')),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^$', views.index),
]
