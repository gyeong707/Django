from django.urls import path, re_path, include
from . import views
from . import views_cbv

app_name = 'dojo'

urlpatterns = [
    
    path('new/', views.post_new),
    path('<int:id>/edit/', views.post_edit),
    path('<pk>/', views.post_detail),

    # path('sum/<int:x>', views.mysum),
    # path('sum/<int:x>/<int:y>', views.mysum),
    # path('sum/<int:x>/<int:y>/<int:z>', views.mysum),
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)$', views.hello),


    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
    path('list3/', views.post_list3),
    path('excel/', views.excel_download),


    path('cbv/list1/', views_cbv.post_list1),
    path('cbv/list2/', views_cbv.post_list2),
    path('cbv/list3/', views_cbv.post_list3),
    path('cbv/excel/', views_cbv.ExcelDownloadView),
]   
