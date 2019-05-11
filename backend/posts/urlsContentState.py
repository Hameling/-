from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentstateList.as_view()),
    path('<pk>/', views.ContentstateDetail.as_view()),
    path(r'^create-contentstate/$', views.ContentstateCreate.as_view()),
]