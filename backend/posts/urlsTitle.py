from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.TitleList.as_view()),
    path('<pk>/', views.TitleDetail.as_view()),
    path(r'^create-title/$', views.TitleCreate.as_view()),
]