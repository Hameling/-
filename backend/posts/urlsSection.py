from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.SectionList.as_view()),
    path('create-section/', views.SectionCreate.as_view()),
    path('search-section/<pk>/', views.SectionSearch.as_view()),
    path('delete-section/<pk>/', views.SectionDelete.as_view()),
    path('update-section/<pk>/', views.SectionUpdate.as_view()),
    path('my-section/<sectionid>', views.MySection.as_view()),
]