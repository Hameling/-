from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChecklistList.as_view()),
    path('create-checklist/', views.ChecklistCreate.as_view()),
    path('search-checklist/<pk>/', views.ChecklistSearch.as_view()),
]