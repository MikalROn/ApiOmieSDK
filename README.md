

# Api Omie SDK

<em>*Aviso: Este projeto não tem ligação oficial com a Omie</em>

> SDK Multi Linguagem para integrar com a Omie API

![License](https://img.shields.io/github/license/MikalROn/ApiOmie-nao-oficial.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dd/api-omie)
![GitHub License](https://img.shields.io/github/license/MikalROn/ApiOmieSDK)
![GitHub contributors](https://img.shields.io/github/contributors/MikalROn/ApiOmieSDK)
![GitHub Repo stars](https://img.shields.io/github/stars/MikalROn/ApiOmieSDK)
[![Documentation Status](https://img.shields.io/badge/docs-latest-blue)](https://MikalROn.github.io/ApiOmieSDK/)


## Documentação Oficial da Omie

Recomendamos sempre consultar a documentação oficial da Omie para detalhes completos das funções disponíveis:

[Omie API - Documentação Oficial](https://developer.omie.com.br/service-list/)

## Instalação (Python)

Para instalar o pacote da Omie via `pip`, use o seguinte comando:

```bash
pip install api-omie
```

## Como usar

Veja abaixo como fazer uma chamada básica para listar produtos usando a Omie API.

### Exemplo de uso básico

```python
from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret')
response = omie_app.listar_produtos(pagina=1)

print(response)
```

Os metodos se encontram neste formato `nome_da_chamada(**argumentos)`


## Usando Sessões para Melhor Desempenho

Se você for fazer várias requisições à API, é altamente recomendado usar uma sessão para reutilizar a conexão e reduzir o overhead de abrir novas conexões a cada chamada. Veja como abrir e fechar uma sessão:

```python
from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret', session=True)
response = omie_app.listar_produtos(pagina=1)
omie_app.fechar_session()

print(response)
```
O SDK também oferece suporte ao uso de gerenciador de contexto para abrir e fechar sessões automaticamente. Todas as chamadas com gerenciador de contexto tem por padrão o uso da sessão.

```python
from omieapi import Omie
omie_app = Omie('sua_app_key', 'seu_app_secret')

with omie_app as r:
    response = r.listar_produtos(pagina=1)

print(response)
```

É possível abrir uma sessão utilizando o metodo `Omie.abrir_sessão()`

### Exemplo de uso com `httpx`

```python
from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret', use_httpx=True)
response = omie_app.listar_produtos(pagina=1)

print(response)

```

### Ativando Logs para Depuração

```python
from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret', log=True)
response = omie_app.listar_produtos(pagina=1)

print(response)

```


## Contribua com este Projeto

Estamos sempre em busca de melhorias! Um dos próximos passos para este SDK é torná-lo realmente multi-linguagem, com suporte a diferentes linguagens de programação. Já existe um script de scraping que extrai os tipos complexos da API, mas ainda precisamos de ajuda para gerar o código de maneira automatizada.

### Como Contribuir
- Clone o repositório
- Crie uma nova branch para suas mudanças
- Envie um pull request



