from django.urls import path

from . import views

urlpatterns = [
    path('', views.AssignList.as_view()),
    path('<pk>/', views.AssignDetail.as_view()),
    path(r'^create-assign/$', views.AssignCreate.as_view()),
]