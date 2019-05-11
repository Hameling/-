from django.urls import path

from . import views
import requests

urlpatterns = [
    path('', views.SectionList.as_view()),
    path('<pk>/', views.SectionDetail.as_view()),
    path(r'^create-section/$', views.SectionCreate.as_view()),
]