from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentList.as_view()),
    path('create-content/', views.ContentCreate.as_view()),
    path('search-content/', views.ContentSearch.as_view()),
    path('delete-content/', views.ContentDelete.as_view()),
    path('update-content/', views.ContentUpdate.as_view()),
]