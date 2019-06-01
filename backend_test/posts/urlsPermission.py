from django.urls import path

from . import views
#import requests

urlpatterns = [
    path('', views.PermissionList.as_view()),
    path('create-permission/', views.PermissionCreate.as_view()),
    path('search-permissionmember/', views.PermissionSearchMember.as_view()),   #해당 멤버가 어느 파일 권한을 부여 받았는지
    path('search-permissioncontent/', views.PermissionSearchContent.as_view()),  #해당 컨텐트가 어느 파일에 권한을 부여 했는지
    path('delete-permission/', views.PermissionDelete.as_view()),
]