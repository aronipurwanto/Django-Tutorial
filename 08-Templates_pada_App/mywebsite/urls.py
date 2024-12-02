from django.contrib import admin
from django.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^$', views.index),
]
