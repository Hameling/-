from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentstateList.as_view()),
    path('create-contentstate/', views.ContentstateCreate.as_view()),
    path('search-contentstate/<word>/', views.ContentstateSearch.as_view()),
    path('delete-contentstate/<pk>/', views.ContentstateDelete.as_view()),
    path('update-contentstate/<pk>/', views.ContentstateUpdate.as_view()),
]