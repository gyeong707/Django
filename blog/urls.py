#blog/urls.py
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
#url이 아닌 path 사용