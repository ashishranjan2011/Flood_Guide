"""FloodGuide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include,url
from django.urls import path
from user_response import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
    # url(r'^delete/',views.UserDetail.as_view(), name='delete_event'),
    # url(r'^delete$/(?P<pk>\d+)',views.UserDetail.as_view(), name='delete_event'),
     url(r'^delete/(?P<pk>\d+)/$',views.UserDetail.as_view(), name='delete'),
     url(r'^deletesaver/(?P<pk>\d+)/$',views.SaverDetail.as_view(), name='deletesaver'),
     url(r'^saver/$',views.SaverList.as_view()),
     url(r'^saver/(?P<pk>\d+)/$',views.SaverDetail.as_view()),
     url(r'^getuser/(?P<pk>\d+)/$',views.SaverDetail.as_view(), name='getuser'),
     # url(r'^chngstatus/',views.changestatus,name='chngstatus')
     # url(r'^edit/(?P<*args>+?P<)
]
