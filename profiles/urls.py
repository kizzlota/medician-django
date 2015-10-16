
from django.conf.urls import url

urlpatterns = [
	url(r'^$', 'profiles.views.index', name='index'),

]
