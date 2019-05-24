from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalenderList.as_view()),
    path('create-calender/', views.CalenderCreate.as_view()),
    path('search-calender/', views.CalenderSearch.as_view()),
    path('delete-calender/', views.CalenderDelete.as_view()),
    path('update-calender/', views.CalenderUpdate.as_view()),
]