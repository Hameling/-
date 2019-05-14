from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.TitleList.as_view()),
    path('create-title/', views.TitleCreate.as_view()),
    path('search-title/<pk>/', views.TitleSearch.as_view()),
]