from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentList.as_view()),
    path('create-content/', views.ContentCreate.as_view()),
    path('search-content/<pk>/', views.ContentSearch.as_view()),
    path('delete-content/<pk>/', views.ContentDelete.as_view()),
    path('update-content/<pk>/', views.ContentUpdate.as_view()),
    path('my-content/<sectionid>/', views.MyContent.as_view()), #어떤 section에 어떤 content가 들어가 있는지 확인
]