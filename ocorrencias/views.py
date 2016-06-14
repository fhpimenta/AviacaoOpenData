from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Ocorrencia

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