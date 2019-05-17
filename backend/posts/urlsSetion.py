from django.urls import path

from . import views

urlpatterns = [
    path('', views.SetionList.as_view()),
    path('create-setion/', views.SetionCreate.as_view()),
    path('search-setion/<pk>/', views.SetionSearch.as_view()),
    path('delete-setion/<pk>/', views.SetionDelete.as_view()),
]