from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentstateList.as_view()),
    path('create-contentstate/', views.ContentstateCreate.as_view()),
    path('search-contentstate/<pk>/', views.ContentstateSearch.as_view()),
]