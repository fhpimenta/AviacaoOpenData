from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ocorrencias/ano$', views.ocorrencias_por_ano),
	url(r'^ocorrencias/aeronave$', views.page_por_tipo_aeronave),
	url(r'^ocorrencias/async/aeronave$', views.ocorrencias_por_tipo_aeronave),
	url(r'^ocorrencias/historico$', views.page_historico),

	# urls async
	url(r'^ocorrencias/async/historico$', views.get_ocorrencias_historico),
]