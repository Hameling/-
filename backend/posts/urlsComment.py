from django.urls import path

from . import views

urlpatterns = [
    path('', views.CommentList.as_view()),
    path('create-comment/', views.CommentCreate.as_view()),
    path('search-comment/<pk>/', views.CommentSearch.as_view()),
]