from django.urls import path

from . import views

urlpatterns = [
    path('', views.PermissionstateList.as_view()),
    path('create-permissionstate/', views.PermissionstateCreate.as_view()),
    path('search-permissionstate/<pk>/', views.PermissionstateSearch.as_view()),
]