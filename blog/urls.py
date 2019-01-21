#blog/urls.py
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.post_list),
]