from django.urls import path

from . import views

urlpatterns = [
    path('', views.EnrollList.as_view()),
    path('create-enroll/', views.EnrollCreate.as_view()),
    path('search-enroll/<pk>/', views.EnrollSearch.as_view()),
]