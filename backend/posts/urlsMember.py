from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.MemberList.as_view()),
    path('create-member/', views.MemberCreate.as_view()),
    path('delete-member/', views.MemberDelete.as_view()),
    path('update-member/', views.MemberUpdate.as_view()),
    path('call-all/', views.SearchAll.as_view()),
    path('search-member/',views.MemberSearch.as_view()),
]