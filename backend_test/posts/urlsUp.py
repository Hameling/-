from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.UpList.as_view()),
    path('upload/',views.Upload.as_view(),)
]