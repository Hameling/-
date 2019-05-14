from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.SectionList.as_view()),
    path('create-section/', views.SectionCreate.as_view()),
    path('search-section/<pk>/', views.SectionSearch.as_view()),
]