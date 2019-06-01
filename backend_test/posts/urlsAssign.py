from django.urls import path

from . import views

urlpatterns = [
    path('', views.AssignList.as_view()),
    path('create-assign/', views.AssignCreate.as_view()),
    path('search-assignmember/', views.AssignSearchMember.as_view()), #해당 member가 어느 content에 할당 되어 있는가
    path('search-assigncontent/', views.AssignSearchContent.as_view()), #해당 content에 어느 member가 할당 되어 있는가
    path('delete-assign/', views.AssignDelete.as_view()),
]