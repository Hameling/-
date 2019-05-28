from django.urls import path

from . import views

urlpatterns = [
    path('', views.SessionList.as_view()),
    path('create-session/', views.SessionCreate.as_view()),
]