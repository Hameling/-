from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.PermissionList.as_view()),
    path('create-permission/', views.PermissionCreate.as_view()),
    path('search-permission/<pk>/', views.PermissionSearch.as_view()),
]