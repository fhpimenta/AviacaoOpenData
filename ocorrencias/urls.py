from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ocorrencias/ano$', views.ocorrencias_por_ano),
	url(r'^ocorrencias/aeronave$', views.page_por_tipo_aeronave),	
	url(r'^ocorrencias/historico$', views.page_historico),
	url(r'^ocorrencias/estado$', views.page_ocorrencias_por_estado),
	url(r'^ocorrencias/geral$', views.page_ocorrencias_geral),
	url(r'^ocorrencias/show/(?P<codigo>[0-9]{5})/$', views.show_ocorrencia),
	url(r'^ocorrencias/tipos$', views.page_tipos_ocorrencia),

	# urls async
	url(r'^ocorrencias/async/historico$', views.get_ocorrencias_historico),
	url(r'^ocorrencias/async/aeronave$', views.ocorrencias_por_tipo_aeronave),
	url(r'^ocorrencias/async/estado$', views.get_ocorrencias_estado),
	url(r'^ocorrencias/async/geral/estados$', views.get_relatorio_ocorrencias_estados),
	url(r'^ocorrencias/async/tipos$', views.get_relatorio_tipos_ocorrencia),
]