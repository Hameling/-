from django.urls import path

from . import views

urlpatterns = [
    path('', views.AssignList.as_view()),
    path('create-assign/', views.AssignCreate.as_view()),
    path('search-assign/', views.AssignSearch.as_view()),
    path('delete-assign/', views.AssignDelete.as_view()),
]