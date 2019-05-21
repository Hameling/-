"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assign/', include('posts.urlsAssign')),
    path('calender/', include('posts.urlsCalender')),
    path('checklist/', include('posts.urlsChecklist')),
    path('comment/', include('posts.urlsComment')),
    path('content/', include('posts.urlsContent')),
    path('contentstate/', include('posts.urlsContentState')),
    path('enroll/', include('posts.urlsEnroll')),
    path('file/', include('posts.urlsFile')),
    path('member/', include('posts.urlsMember')),
    path('permission/', include('posts.urlsPermission')),
    path('section/', include('posts.urlsSection')),
    path('title/', include('posts.urlsTitle')),
    path('permissionstate/', include('posts.urlsPermissionstate')),
    path('session/', include('posts.urlsSession')),
    #테스트
    path('forms/', include('posts.forms')),
]

#테스트
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)