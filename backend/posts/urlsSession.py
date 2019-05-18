from django.urls import path

from . import views

urlpatterns = [
    path('', views.SessionList.as_view()),
    path('create-setion/', views.SessionCreate.as_view()),
    path('search-setion/<pk>/', views.SessionSearch.as_view()),
    path('delete-setion/<pk>/', views.SessionDelete.as_view()),
]