from django.urls import path

from . import views

urlpatterns = [
    path('', views.PermissionstateList.as_view()),
    path('<pk>/', views.PermissionstateDetail.as_view()),
    path(r'^create-permissionstate/$', views.PermissionstateCreate.as_view()),
]