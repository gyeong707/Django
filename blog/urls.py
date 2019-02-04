#blog/urls.py
from django.urls import re_path, path
from . import views
from . import views_cbv


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('cbv/', views_cbv.post_list),

    path('<int:id>/', views.post_detail, name='post_detail'),
    path('cbv/<pk>/', views_cbv.post_detail),

    path('<int:id>/edit/', views.post_edit, name='post_edit'),
    path('cbv/<pk>/edit/', views_cbv.post_edit),


    path('new/', views.post_new, name='post_new'),
    path('cbv/new/', views_cbv.post_new),

    path('cbv/<pk>/delete/', views_cbv.post_delete),
]
