# Dados Abertos de Ocorrencias Aeronáuticas da Aviação Civil Brasileira

Este projeto utiliza os dados abertos de ocorrencias aeronáuticas (acidentes, incidentes) que ocorreram nos ultimos 10 anos na Aviação Civil Brasileira.

O projeto é implementado em Python 3, utilizando o framework web [Django](https://www.djangoproject.com/).

Para utilização do projeto é necessário ter o Python 3 e o Django instalado na máquina.

### Instalação

Ao clonar o projeto, entre na pasta do projeto, e dê o seguinte comando:

```sh
$ python3 manage.py migrate
```

Para acessar a aplicação, utilize o servidor web embutido no Django, com o seguinte comando:

```sh
$ python3 manage.py runserver
```