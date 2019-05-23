from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.MemberList.as_view()),
    path('create-member/', views.MemberCreate.as_view()),
    path('search-member/<pk>/', views.MemberSearch.as_view()),
    path('delete-member/<pk>/', views.MemberDelete.as_view()),
    path('update-member/<pk>/', views.MemberUpdate.as_view()),
    path('call-all/', views.SearchAll.as_view()),
    path('login/',views.Login.as_view()),
]