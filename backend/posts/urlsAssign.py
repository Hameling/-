from django.urls import path

from . import views

urlpatterns = [
    path('', views.AssignList.as_view()),
    path('create-assign/', views.AssignCreate.as_view()),
    path('search-assign/<pk>/', views.AssignSearch.as_view()),
    path('delete-assign/<pk>/', views.AssignDelete.as_view()),
    path('update-assign/<pk>/', views.AssignUpdate.as_view()),
    path('my-assign/<memberid>', views.MyAssign.as_view()), #내가 어느 content에 할당되어 있는가 확인
]