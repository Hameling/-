from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalenderList.as_view()),
    path('create-calender/', views.CalenderCreate.as_view()),
    path('search-calender/<pk>/', views.CalenderSearch.as_view()),
    path('delete-calender/<pk>/', views.CalenderDelete.as_view()),
    path('update-calender/<pk>/', views.CalenderUpdate.as_view()),
]