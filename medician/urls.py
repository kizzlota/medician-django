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
from interrealation import views as inter_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	url('', include('social.apps.django_app.urls', namespace='social')),

    # url(r'^', include(router.urls)),
    url(r'^api/account/registration/', views.AccountViewSet.as_view({'post': 'create'}), name='account_viewset'),
    url(r'^api/account/login/', views.AccountLogin.as_view({'post': 'login'}), name='user_login'),

	url(r'^api/account/user_details/', views.UserBioViewSet.as_view({'get': 'list', 'post': 'create'}), name='list_user_details'),
    url(r'^api/account/user_details/(?P<id>[0-9]+)/$', views.UserBioViewSet.as_view({'post': 'create', 'get': 'list'}), name='user_details'),

	url(r'^api/account/user_address/', views.UserAddressViewSet.as_view({'get': 'list', 'post': 'create'}),name='list_user_address'),
	url(r'^api/account/user_address/(?P<id>[0-9]+)/$', views.UserAddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_address'),

    url(r'^api/account/user_analyzes/(?P<id>[0-9]+)/$', views.UserAnalyzesViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_analyzes'),
    url(r'^api/account/user_analyzes/', views.UserAnalyzesViewSet.as_view({'get': 'list', 'post': 'create'}), name='list_user_analyzes'),

	url(r'^api/account/user_files/', views.UserFilesViewSet.as_view({'get': 'list', 'post': 'create'}), name='list_user_files'),
    url(r'^api/account/user_files/(?P<id>[0-9]+)/$', views.UserFilesViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_files'),


	url(r'^api/quick_post/(?P<id>[0-9]+)/$', inter_view.QuickPostViewSet.as_view({'get': 'list', 'post': 'create'}),
	    name='list_posts'),
	url(r'^api/quick_post/', inter_view.QuickPostViewSet.as_view({'get': 'list', 'post': 'create'}), name='quick_post'),

    url(r'^tester/', views.tester, name='tester'),
    url(r'^tester2/', views.tester2, name='tester2'),
    url(r'^tester3/', views.tester3, name='tester3'),

	url(r'^$', views.index, name='index'),


]
