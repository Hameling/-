from django.urls import path

from . import views

urlpatterns = [
    path('', views.FileList.as_view()),
    path('create-file/', views.FileCreate.as_view()),
    path('search-file/<pk>/', views.FileSearch.as_view()),
]