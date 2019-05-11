from django.urls import path

from . import views

urlpatterns = [
    path('', views.EnrollList.as_view()),
    path('<pk>/', views.EnrollDetail.as_view()),
    path(r'^create-enroll/$', views.EnrollCreate.as_view()),
]