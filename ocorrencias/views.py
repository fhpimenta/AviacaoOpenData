from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Ocorrencia, Aeronave
from decimal import *

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def ocorrencias_por_ano(request):
	retorno = {}
	anos = []
	quant_acidentes = []
	quant_incidentes_graves = []

	ano = 2006
	for i in range(10):
		acidentes = Ocorrencia.objects.filter(dia_ocorrencia__year=ano,classificacao="ACIDENTE")
		incidentes_graves = Ocorrencia.objects.filter(dia_ocorrencia__year=ano,classificacao="INCIDENTE GRAVE")
		anos.append(ano)
		quant_acidentes.append(len(acidentes))
		quant_incidentes_graves.append(len(incidentes_graves))

		ano += 1

	retorno['anos'] = anos
	retorno['quant_acidentes'] = quant_acidentes
	retorno['quant_incidentes_graves'] = quant_incidentes_graves

	return JsonResponse(retorno, safe=False)

def page_por_tipo_aeronave(request):
	return render(request, 'ocorrencias_aeronave.html', {})

def page_ocorrencias_por_estado(request):
	return render(request, 'ocorrencias_estado.html', {})

def ocorrencias_por_tipo_aeronave(request):
	tipos_aeronaves = ['AVIÃO', 'HELICÓPTERO', 'PLANADOR', 'ANFÍBIO', 'ULTRALEVE', 'EXPERIMENTAL']
	quant_tipo = []

	total_ocorrencias = 0
	for tipo in tipos_aeronaves:
		quant = Aeronave.objects.filter(equipamento=tipo).count()
		quant_tipo.append(quant)
		total_ocorrencias += quant

	resultados = {}
	for i in range(len(tipos_aeronaves)):
		# calcular a porcentagem de ocorrencias de cada tipo
		percent = percentagem(quant_tipo[i], total_ocorrencias)
		percent = Decimal(str(percent)).quantize(Decimal('1.0'))

		resultados[tipos_aeronaves[i]] = float(percent)

	items = [(v,k) for k,v in resultados.items()]
	items.sort()
	retorno = [(k,v) for v,k in items]

	return JsonResponse(retorno, safe=False)

def page_historico(request):
	ocorrencias = Ocorrencia.objects.all()
	return render(request, 'historico.html', {'ocorrencias': ocorrencias})

def get_ocorrencias_historico(request):

	ocorrencias = Ocorrencia.objects.all()	

	if request.method == 'POST':
		estado = request.POST['uf']
		ano = int(request.POST['ano'])
		if request.POST['uf'] != 0:
			ocorrencias = ocorrencias.filter(uf=estado)
		if request.POST['ano'] != 0:
			ocorrencias = ocorrencias.filter(dia_ocorrencia__year=ano)

	retorno = {'data':[]}
	print(ocorrencias)
	for oc in ocorrencias:
		linha = []
		linha = [oc.codigo_ocorrencia,oc.classificacao,oc.tipo,oc.localidade,oc.uf, "{:%d/%m/%Y}".format(oc.dia_ocorrencia)]
		retorno['data'].append(linha)
		

	return JsonResponse(retorno, safe=False)

def get_ocorrencias_estado(request):
	uf = request.GET['uf']

	retorno = {}
	anos = []
	quant_acidentes = []
	quant_incidentes_graves = []

	ano = 2006
	for i in range(10):
		acidentes = Ocorrencia.objects.filter(dia_ocorrencia__year=ano,classificacao="ACIDENTE",uf=uf)
		incidentes_graves = Ocorrencia.objects.filter(dia_ocorrencia__year=ano,classificacao="INCIDENTE GRAVE",uf=uf)
		anos.append(ano)
		quant_acidentes.append(len(acidentes))
		quant_incidentes_graves.append(len(incidentes_graves))

		ano += 1

	retorno['anos'] = anos
	retorno['quant_acidentes'] = quant_acidentes
	retorno['quant_incidentes_graves'] = quant_incidentes_graves

	return JsonResponse(retorno, safe=False)

def percentagem(valor, total):
	return float((valor*100)/total)