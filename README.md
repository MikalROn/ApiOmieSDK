# Api Omie (NÃO OFICIAL)

<em> *Aviso: este projeto não tem ligação nenhuma com a omie</em>

# Use a documentação oficial!

## download

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
