from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.PermissionList.as_view()),
    path('<pk>/', views.PermissionDetail.as_view()),
    path(r'^create-permission/$', views.PermissionCreate.as_view()),
]