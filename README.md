# Api Omie (NÃO OFICIAL)

<em> *Aviso: este projeto não tem ligação nenhuma com a omie</em>

![!license](https://camo.githubusercontent.com/92b715ac5f55013c8ec6a518478dfd86491cdf5fb140ff237055967299c36390/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4d696b616c524f6e2f4576656e7453696d706c654755493f7374796c653d666f722d7468652d6261646765)

<a href="https://github.com/MikalROn/ApiOmie-nao-oficial">
<img alt="GitHub" src="https://img.shields.io/badge/Github-Open%20source-green?style=for-the-badge&amp;logo=github"/>
</a>

# ⚠ Use a documentação oficial!

## Download

``````shell
$pip install api-omie
``````

## como usar

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
