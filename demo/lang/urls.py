from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^add/$', views.add_language, name='add_language'),
	url(r'^$', views.index, name='index'),
#	url(r'^list/$', views.list_language, name='list_language'),
	
]
