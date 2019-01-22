from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('sum/<int:x>', views.mysum),
    path('sum/<int:x>/<int:y>', views.mysum),
    path('sum/<int:x>/<int:y>/<int:z>', views.mysum),

]