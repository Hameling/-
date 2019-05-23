from django.urls import path

from . import views

urlpatterns = [
    path('', views.EnrollList.as_view()),
    path('create-enroll/', views.EnrollCreate.as_view()),
    path('search-enrollmember/', views.EnrollSearchMember.as_view()), #해당 타이틀에 누가 들어갔는가
    path('search-enrolltitle/', views.EnrollSearchTitle.as_view()), #내가 어느 타이틀에 들어갔는가
    path('delete-enroll/', views.EnrollDelete.as_view()),
]