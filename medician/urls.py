"""medician URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from profiles import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   # url(r'^$', 'profiles.views.registration', name='registration'),
    url(r'^', include(router.urls)),
    url(r'^api/account/registration/', views.AccountViewSet.as_view({'post': 'create'})),
    url(r'^api/account/login/', views.AccountLogin.as_view({'post': 'login'})),
    url(r'^api/account/user_details/', views.UserQuestionnaireViewSet.as_view({'get': 'list'})),
    url(r'^api/account/add/user_details/', views.UserQuestionnaireViewSet.as_view({'post': 'create', 'get': 'list'})),
    url(r'^tester/', 'profiles.views.tester', name='tester'),
    url(r'^tester2/', 'profiles.views.tester2', name='tester2'),
    url(r'^tester3/', 'profiles.views.tester3', name='tester3'),


]
