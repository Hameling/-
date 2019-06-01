from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChecklistList.as_view()),
    path('create-checklist/', views.ChecklistCreate.as_view()),
    path('search-checklist/', views.ChecklistSearch.as_view()),
    path('delete-checklist/', views.ChecklistDelete.as_view()),
    path('update-checklist/', views.ChecklistUpdate.as_view()),
]