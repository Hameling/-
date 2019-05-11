from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.MemberList.as_view()),
    path('<pk>/', views.MemberDetail.as_view()),
    path(r'^create-member/$', views.MemberCreate.as_view()),
    path(r'^search-member/$<pk>', views.MemberSearch.as_view()),
]