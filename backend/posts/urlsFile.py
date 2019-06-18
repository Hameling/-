from django.urls import path

from . import views

urlpatterns = [
    path('', views.FileList.as_view()),
    path('create-file/', views.FileCreate.as_view()),
    path('down-file/', views.FileDownload.as_view()),
    path('search-file/', views.FileSearch.as_view()),
]