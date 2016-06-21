from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import urllib.request
import json
from .models import Ocorrencia, Aeronave, FatorContribuinte
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

def page_ocorrencias_geral(request):
	return render(request, 'ocorrencias_geral.html', {})

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

	retorno = sort_dict(resultados)

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
		linha.append('<a class="btn btn-primary" href="/ocorrencias/show/'+str(oc.codigo_ocorrencia)+'"><i class="fa fa-eye"></i></a>')
		#linha = {}
		#linha['codigo'] = oc.codigo_ocorrencia
		#linha['classificacao'] = oc.classificacao
		#linha['tipo'] = oc.tipo
		#linha['localidade'] = oc.localidade
		#linha['estado'] = oc.estado
		#linha['diaDaOcorrencia'] = "{:%d/%m/%Y}".format(oc.dia_ocorrencia)
		#linha['opcoes'] = "<a class='btn btn-primary' href='#'></a>"
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

def get_relatorio_ocorrencias_estados(request):

	estados = {
		"AC": "Acre",
		"AL": "Alagoas",
		"AP": "Amapá",
		"AM": "Amazonas",
		"BA": "Bahia",
		"CE": "Ceará",
		"DF": "Distrito Federal",
		"ES": "Espirito Santo",
		"GO": "Goiás",
		"MA": "Maranhão",
		"MT": "Mato Grosso",
		"MS": "Mato Grosso do Sul",
		"MG": "Minas Gerais",
		"PA": "Pará",
		"PB": "Paraíba",
		"PR": "Paraná",
		"PE": "Pernambuco",
		"PI": "Piauí",
		"RJ": "Rio de Janeiro",
		"RN": "Rio Grande do Norte",
		"RS": "Rio Grande do Sul",
		"RO": "Rondônia",
		"RR": "Roraima",
		"SC": "Santa Catarina",
		"SP": "São Paulo",
		"SE": "Sergipe",
		"TO": "Tocantins"
	}

	total_ocorrencias = 0
	retorno = {}
	arrEstados = []
	arrQuant = []
	for uf in estados.keys():
		quant = Ocorrencia.objects.filter(uf=uf, dia_ocorrencia__year__range=(2006,2015)).count()
		arrEstados.append(estados[uf])
		arrQuant.append(quant)
		total_ocorrencias += quant

	# calcular porcentagem por estado
	for i in range(len(arrQuant)):
		# calcular a porcentagem de ocorrencias de cada tipo
		percent = percentagem(arrQuant[i], total_ocorrencias)
		percent = Decimal(str(percent)).quantize(Decimal('1.0'))

		#arrQuant[i] = float(percent)
		retorno[arrEstados[i]] = float(percent)

	#retorno['estados'] = arrEstados
	#retorno['quant'] = arrQuant
	retorno = sort_dict(retorno)

	return JsonResponse(retorno, safe=False)

def show_ocorrencia(request, codigo):
	ocorrencia = Ocorrencia.objects.get(pk=codigo)
	aeronaves = Aeronave.objects.filter(codigo_ocorrencia=codigo)
	fatores = FatorContribuinte.objects.filter(codigo_ocorrencia=codigo)
	#url = "http://ocorrencias-aviacao-api.herokuapp.com/api/ocorrencias/"+str(codigo)
	#print(url)
	#response = urllib.request.urlopen(url).read()
	#ocorrencia = json.loads(response.decode('utf-8'))
	return render(request, 'ocorrencia_show.html', {'ocorrencia': ocorrencia, 'aeronaves': aeronaves, 'fatores': fatores})

def percentagem(valor, total):
	return float((valor*100)/total)

def sort_dict(dictionary,order='desc'):
	items = [(v,k) for k,v in dictionary.items()]
	if(order == 'desc'):
		items.sort(reverse=True)
	else:
		items.sort()
	
	retorno = [(k,v) for v,k in items]

	return retorno