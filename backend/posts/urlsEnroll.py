from django.urls import path

from . import views

urlpatterns = [
    path('', views.EnrollList.as_view()),
    path('create-enroll/', views.EnrollCreate.as_view()),
    path('search-enroll/<pk>/', views.EnrollSearch.as_view()),
    path('delete-enroll/<pk>/', views.EnrollDelete.as_view()),
    path('update-enroll/<pk>/', views.EnrollUpdate.as_view()),
    path('my-enroll/<memberid>', views.MyEnroll.as_view()),
    path('my-title/<titleid>', views.MyTitle.as_view()),
]