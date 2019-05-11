from django.urls import path

from . import views

urlpatterns = [
    path('', views.CommentList.as_view()),
    path('<pk>/', views.CommentDetail.as_view()),
    path(r'^create-comment/$', views.CommentCreate.as_view()),
]