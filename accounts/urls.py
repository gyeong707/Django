from django.urls import path, re_path, include
from . import views

app_name = 'accounts'

urlpatterns= [
    path('profile/', views.profile),
]