from django.urls import path

from . import views

urlpatterns = [
    path('', views.FileList.as_view()),
    path('<pk>/', views.FileDetail.as_view()),
    path(r'^create-file/$', views.FileCreate.as_view()),
]