from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.SectionList.as_view()),
    path('create-section/', views.SectionCreate.as_view()),
    path('search-section/', views.SectionSearch.as_view()),
    path('delete-section/', views.SectionDelete.as_view()),
    path('update-section/', views.SectionUpdate.as_view()),
]