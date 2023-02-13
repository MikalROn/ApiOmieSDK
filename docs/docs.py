import pydoc
from flask import Flask
from omieapi import Conta, Produtos, Omie

app = Flask(__name__)

doc = f'<h1 aling="center" > APi Omie  </h1>'\
      f'{pydoc.html.docclass(Omie)}' \
      f'{pydoc.html.docclass(Produtos)}' \
      f'{pydoc.html.docclass(Conta)}'

@app.route('/')
def index():
    return doc

app.run(debug=True)