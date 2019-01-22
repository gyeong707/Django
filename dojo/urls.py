from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # path('sum/<int:x>', views.mysum),
    # path('sum/<int:x>/<int:y>', views.mysum),
    # path('sum/<int:x>/<int:y>/<int:z>', views.mysum),
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),

    #이거 그냥 path로는 어떻게 쓰지? Converter 이용하는건가??
    
]