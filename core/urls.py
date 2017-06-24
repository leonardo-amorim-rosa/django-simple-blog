from django.conf.urls import url
from core import views 

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^new/$', views.new, name="new"),
	url(r'^update/(?P<id>\d+)$', views.update, name="update"),
	url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
]