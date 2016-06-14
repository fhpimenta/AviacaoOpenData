# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import urllib.request
import csv

def add_ocorrencias(apps, schema_editor):
	response = urllib.request.urlopen("http://www.cenipa.aer.mil.br/cenipa/Anexos/article/1451/ocorrencia.csv")
	ocorrencias_csv = csv.DictReader(response.read().decode('utf-8').splitlines())
	
	Ocorrencia = apps.get_model('ocorrencias', 'Ocorrencia')
	for row in ocorrencias_csv:		
		ocorrencia = Ocorrencia(
			codigo_ocorrencia=row['codigo_ocorrencia'],
			classificacao=row['classificacao'],
			tipo=row['tipo'],
			localidade=row['localidade'],
			uf=row['uf'],
			pais=row['pais'],
			dia_ocorrencia=row['dia_ocorrencia'],
			horario_utc=row['horario'],
			comando_investigador=row['comando_investigador'],
			quantidade_recomendacoes=row['quantidade_recomendacoes'],
			aeronaves_envolvidas=row['aeronaves_envolvidas'],
			dia_extracao=row['dia_extracao']
		)

		if(row['aerodromo'] != "****"):
			ocorrencia.aerodromo = row['aerodromo']

		if(row['sera_investigada'] != "***"):
			ocorrencia.sera_investigada = row['sera_investigada']

		if(row['status_investigacao'] != 'NULL'):			
			ocorrencia.status_investigacao = row['status_investigacao']

		if(row['numero_relatorio'] != 'NULL'):
			ocorrencia.numero_relatorio = row['numero_relatorio']

		if(row['relatorio_publicado'] != 'NULL'):
			ocorrencia.relatorio_publicado = row['relatorio_publicado']

		if(row['dia_publicacao'] != 'NULL'):
			ocorrencia.dia_publicacao = row['dia_publicacao']

		if(row['saida_pista'] != 'NULL'):
			ocorrencia.saida_pista = row['saida_pista']


		ocorrencia.save()

def add_aeronaves(apps, schema_editor):
	response = urllib.request.urlopen("http://www.cenipa.aer.mil.br/cenipa/Anexos/article/1451/aeronave.csv")
	reader = csv.DictReader(response.read().decode('utf-8').splitlines())

	Aeronave = apps.get_model('ocorrencias', 'Aeronave')
	Ocorrencia = apps.get_model('ocorrencias', 'Ocorrencia')
	for row in reader:
		aeronave = Aeronave(
			codigo_aeronave=row['codigo_aeronave'],
			codigo_ocorrencia=Ocorrencia.objects.get(pk=row['codigo_ocorrencia']),
			matricula=row['matricula'],
			codigo_operador=int(row['codigo_operador']),
			equipamento=row['equipamento'],
			fabricante=row['fabricante'],
			modelo=row['modelo'],
			tipo_motor=row['tipo_motor'],
			peso_maximo_decolagem=float(row['peso_maximo_decolagem']),
			pais_registro=row['pais_registro'],
			categoria_registro=row['categoria_registro'],
			categoria_aviacao=row['categoria_aviacao'],
			fase_operacao=row['fase_operacao'],
			tipo_operacao=row['tipo_operacao'],
			dia_extracao=row['dia_extracao']
		)

		if(row['quantidade_assentos'] != 'NULL'):
			aeronave.quantidade_assentos = int(row['quantidade_assentos'])

		if(row['quantidade_motores'] != 'NULL'):
			aeronave.quantidade_motores = int(row['quantidade_motores'])

		if(row['ano_fabricacao'] != 'NULL'):
			aeronave.ano_fabricacao = int(row['ano_fabricacao'])

		if(row['origem_voo'] != '****'):
			aeronave.origem_voo = row['origem_voo']

		if(row['destino_voo'] != '****'):
			aeronave.destino_voo = row['destino_voo']

		if(row['nivel_dano'] != '***'):
			aeronave.nivel_dano = row['nivel_dano']

		if(row['quantidade_fatalidades'] != 'NULL'):
			aeronave.quantidade_fatalidades = int(row['quantidade_fatalidades'])

		aeronave.save()

def add_fatores_contribuintes(apps, schema_editor):
	response = urllib.request.urlopen("http://www.cenipa.aer.mil.br/cenipa/Anexos/article/1451/fator_contribuinte.csv")
	reader = csv.DictReader(response.read().decode('utf-8').splitlines())

	FatorContribuinte = apps.get_model('ocorrencias','FatorContribuinte')
	Ocorrencia = apps.get_model('ocorrencias', 'Ocorrencia')

	for row in reader:
		fator = FatorContribuinte(
			codigo_fator=row['codigo_fator'],
			codigo_ocorrencia=Ocorrencia.objects.get(pk=row['codigo_ocorrencia']),
			fator=row['fator'],
			dia_extracao=row['dia_extracao']
		)

		if(row['aspecto'] != '***'):
			fator.aspecto = row['aspecto']

		if(row['condicionante'] != '***'):
			fator.condicionante = row['condicionante']

		if(row['area'] != '***'):
			fator.area = row['area']

		if(row['detalhe_fator'] != ''):
			fator.detalhe_fator = row['detalhe_fator']

		fator.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencias', '0001_create_tables'),
    ]

    operations = [
    	migrations.RunPython(add_ocorrencias),
    	migrations.RunPython(add_aeronaves),
    	migrations.RunPython(add_fatores_contribuintes),
    ]