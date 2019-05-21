from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views

urlpatterns = [
    path('', views.FileList.as_view()),
    path('create-file/', views.FileCreate.as_view()),
    path('search-file/<pk>/', views.FileSearch.as_view()),
    path('delete-file/<pk>/', views.FileDelete.as_view()),
    path('update-file/<pk>/', views.FileUpdate.as_view()),
    path('fileupload/', views.FileUpload.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)