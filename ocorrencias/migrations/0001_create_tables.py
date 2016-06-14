# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeronave',
            fields=[
                ('codigo_aeronave', models.IntegerField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=10)),
                ('codigo_operador', models.IntegerField()),
                ('equipamento', models.CharField(max_length=45)),
                ('fabricante', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
                ('tipo_motor', models.CharField(max_length=45)),
                ('quantidade_motores', models.IntegerField(default=0)),
                ('peso_maximo_decolagem', models.FloatField()),
                ('quantidade_assentos', models.IntegerField(default=0)),
                ('ano_fabricacao', models.IntegerField(default=0)),
                ('pais_registro', models.CharField(max_length=80)),
                ('categoria_registro', models.CharField(max_length=6)),
                ('categoria_aviacao', models.CharField(max_length=50)),
                ('origem_voo', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('destino_voo', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('fase_operacao', models.CharField(max_length=100)),
                ('tipo_operacao', models.CharField(max_length=30)),
                ('nivel_dano', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('quantidade_fatalidades', models.IntegerField(default=0)),
                ('dia_extracao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FatorContribuinte',
            fields=[
                ('codigo_fator', models.IntegerField(primary_key=True, serialize=False)),
                ('fator', models.CharField(max_length=80)),
                ('aspecto', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('condicionante', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('area', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('detalhe_fator', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('dia_extracao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('codigo_ocorrencia', models.IntegerField(primary_key=True, serialize=False)),
                ('classificacao', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=80)),
                ('localidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=3)),
                ('pais', models.CharField(max_length=80)),
                ('aerodromo', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('dia_ocorrencia', models.DateField()),
                ('horario_utc', models.TimeField()),
                ('sera_investigada', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('comando_investigador', models.CharField(max_length=15)),
                ('status_investigacao', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('numero_relatorio', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('relatorio_publicado', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('dia_publicacao', models.DateField(blank=True, default=None, null=True)),
                ('quantidade_recomendacoes', models.IntegerField(default=0)),
                ('aeronaves_envolvidas', models.IntegerField()),
                ('saida_pista', models.IntegerField(blank=True, default=None, null=True)),
                ('dia_extracao', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='fatorcontribuinte',
            name='codigo_ocorrencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocorrencias.Ocorrencia'),
        ),
        migrations.AddField(
            model_name='aeronave',
            name='codigo_ocorrencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocorrencias.Ocorrencia'),
        ),
    ]