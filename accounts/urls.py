from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .forms import LoginForm


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login_form.html',
        authentication_form = LoginForm), 
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page=settings.LOGIN_URL), name='logout'),
]


    # path('login/', auth_login, name='login', 
    #     kwargs=['template_name':'accounts/login_form.html']),
    # path('logout/', auth_logout, name='logout', 
    #     kwargs={'next_page': settings.LOGIN_URL}),



