<!-- -*- coding: latin-1 -*- -->

# Api Omie (NAO OFICIAL)

<em> *Aviso: este projeto nao tem ligacao nenhuma com a omie</em>

![!license](https://img.shields.io/github/license/MikalROn/ApiOmie-nao-oficial.svg)
<a href="https://github.com/MikalROn/ApiOmie-nao-oficial">
<img alt="GitHub" src="https://img.shields.io/badge/Github-Open%20source-green?style=for-the-badge&amp;logo=github"/>
</a>

#   Use a documentacao oficial!

https://developer.omie.com.br/service-list/

## Download

``````shell
pip install api-omie
``````

## Como usar

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
