from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ocorrencias/ano', views.ocorrencias_por_ano),
]