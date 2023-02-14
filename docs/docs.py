import pydoc
from flask import Flask
from omieapi import Conta, Produtos, Omie, Geral
from omieapi.scripts import CodigoAutoGerado

app = Flask(__name__)

doc = f'<h1 aling="center" > APi Omie  </h1>'\
      f'{pydoc.html.docclass(Omie)}' \
      f'{pydoc.html.docclass(Produtos)}' \
      f'{pydoc.html.docclass(Conta)}' \
      f'{pydoc.html.docclass(Geral)}' \
      f'<h1 aling="center" > Codigo Gerado Automaticamente </h1>'\
      f'{pydoc.html.docclass(CodigoAutoGerado)}'

@app.route('/')
def index():
    return doc

app.run(debug=True)