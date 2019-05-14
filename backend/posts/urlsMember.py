from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.MemberList.as_view()),
    path('create-member/', views.MemberCreate.as_view()),
    path('search-member/<pk>/', views.MemberSearch.as_view()),
]