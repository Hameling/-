from django.urls import path

from . import views

urlpatterns = [
    path('', views.CommentList.as_view()),
    path('create-comment/', views.CommentCreate.as_view()),
    path('delete-comment/', views.CommentDelete.as_view()),
    path('update-comment/', views.CommentUpdate.as_view()),
    path('checkcomment/', views.CheckComment.as_view()),
]