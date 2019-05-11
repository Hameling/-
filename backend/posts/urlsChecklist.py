from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChecklistList.as_view()),
    path('<pk>/', views.ChecklistDetail.as_view()),
    path(r'^create-checklist/$', views.ChecklistCreate.as_view()),
]