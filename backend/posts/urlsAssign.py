from django.urls import path

from . import views

urlpatterns = [
    path('', views.AssignList.as_view()),
    path('create-assign/', views.AssignCreate.as_view()),
    path('search-assign/<pk>/', views.AssignSearch.as_view()),
]