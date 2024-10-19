<!-- -*- coding: latin-1 -*- -->

# Api Omie SDK

<em> *Aviso: este projeto nao tem ligaçãpo nenhuma com a omie</em>

> Projeto Multi Linguagem Omie Api SDK

![!license](https://img.shields.io/github/license/MikalROn/ApiOmie-nao-oficial.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dd/api-omie)
![GitHub License](https://img.shields.io/github/license/MikalROn/ApiOmieSDK)
![GitHub contributors](https://img.shields.io/github/contributors/MikalROn/ApiOmieSDK)
![GitHub Repo stars](https://img.shields.io/github/stars/MikalROn/ApiOmieSDK)


#   Use a documentação oficial!

https://developer.omie.com.br/service-list/

## Python

### Download

``````shell
pip install api-omie
``````

### Como usar

<p> Para usar basta chamar o metodo, 
e passar os argumentos-chave que seram empacotados e transmitidos para api como no exemplo</p>

``````python
from omieapi import Omie

meu_app = Omie('key#######', 'secreet######')

r = meu_app.listar_produtos(
    pagina=1
)

print(r)
``````

# Contribua com este projeto

> Existe já um script na parte de scrap que extrai os tipos compléxos, bastando apenas fazer a parte do codigo.

> Um dos objetivos futuros e se tornar multi-linguagens usando o script para fazer a parte repetitiva do trabalho.
