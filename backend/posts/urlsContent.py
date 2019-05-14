from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentList.as_view()),
    path('create-content/', views.ContentCreate.as_view()),
    path('search-content/<pk>/', views.ContentSearch.as_view()),
]