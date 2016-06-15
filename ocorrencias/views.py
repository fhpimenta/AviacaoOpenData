from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Ocorrencia, Aeronave
from decimal import *

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def ocorrencias_por_ano(request):
	resultados = {}
	anos = []
	quant = []

	ano = 2006
	for i in range(10):
		ocorrencias = Ocorrencia.objects.filter(dia_ocorrencia__year=ano)
		anos.append(ano)
		quant.append(len(ocorrencias))

		ano += 1

	resultados['anos'] = anos
	resultados['quant'] = quant

	return JsonResponse(resultados, safe=False)

def page_por_tipo_aeronave(request):
	return render(request, 'ocorrencias_aeronave.html', {})

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


def percentagem(valor, total):

	return float((valor*100)/total)