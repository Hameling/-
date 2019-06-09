from django.urls import path

from . import views

urlpatterns = [
    path('', views.EnrollList.as_view()),
    path('create-enroll/', views.EnrollCreate.as_view()),
    path('search-enrollmember/', views.EnrollSearchMember.as_view()), 
    path('search-enrolltitle/', views.EnrollSearchTitle.as_view()), 
    path('delete-enroll/', views.EnrollDelete.as_view()),
    path('join-enroll/', views.EnrollJoin.as_view()),
]