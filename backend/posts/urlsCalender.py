from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalenderList.as_view()),
    path('<pk>/', views.CalenderDetail.as_view()),
    path(r'^create-calender/$', views.CalenderCreate.as_view()),
]