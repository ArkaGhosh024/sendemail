from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^graph$', views.graph, name='graph'),
]