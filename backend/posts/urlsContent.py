from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentList.as_view()),
    path('<pk>/', views.ContentDetail.as_view()),
    path(r'^create-content/$', views.ContentCreate.as_view()),
]