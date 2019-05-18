from django.urls import path

from . import views

urlpatterns = [
    path('', views.EnrollList.as_view()),
    path('create-enroll/', views.EnrollCreate.as_view()),
    path('search-enroll/<pk>/', views.EnrollSearch.as_view()),
    path('delete-enroll/<pk>/', views.EnrollDelete.as_view()),
    path('update-enroll/<pk>/', views.EnrollUpdate.as_view()),
    path('my-enroll/<memberid>', views.MyEnroll.as_view()), #memberid가 어느 title에 가입되어 있는지 확인
    path('in-title/<titleid>', views.InTitle.as_view()), #title에 어떤 memberid가 있는지 확인
]