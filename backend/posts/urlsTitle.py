from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.TitleList.as_view()),
    path('create-title/', views.TitleCreate.as_view()),
    path('search-title/', views.TitleSearch.as_view()),
    path('delete-title/', views.TitleDelete.as_view()),
    path('update-title/', views.TitleUpdate.as_view()),
]