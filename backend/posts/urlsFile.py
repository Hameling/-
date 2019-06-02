from django.urls import path

from . import views

urlpatterns = [
    path('', views.FileList.as_view()),
    path('create-file/', views.FileCreate.as_view()),
    #path('search-file/', views.FileSearch.as_view()),
    #path('delete-file/', views.FileDelete.as_view()),
    #path('update-file/', views.FileUpdate.as_view()),
]