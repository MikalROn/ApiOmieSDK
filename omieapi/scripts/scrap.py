from requests import get
from bs4 import BeautifulSoup
import ast
import re
import pandas
import json

# Atenção -> Ao rodar este codigo é gerado um novo codigo automatico
# Não roda ao importar


def pega_links_api():
    """ Captura todos os links da api atravez do link """
    def retquest_devpageomie() -> BeautifulSoup:
        try:
            r = get('https://developer.omie.com.br/service-list/')
            r.raise_for_status()
            return BeautifulSoup(r.text, features="html.parser")
        except:
            raise Exception('Erro na requisição')
    suop = retquest_devpageomie().find('div', {'class': 'service-list'})
    return {
        item.get_text().strip(): item.get("href")
        for item in suop.find_all('a')
    }


def retorna_divs_de_metodos(url: str):
    def request_omieapi(url: str) -> BeautifulSoup:
        try:
            r = get(url, headers={'Content-type': 'text/html; charset=UTF-8'})
            r.raise_for_status()
            return BeautifulSoup(r.text, features="html.parser")
        except:
            raise Exception('Erro na requisição')
    soap = request_omieapi(url)
    return soap.find_all('div', {'class': 'methodItem'})


def pegar_todos_os_metodos(urls: list[str]):
    dicionario_final = {}
    for url in urls:
        for item in retorna_divs_de_metodos(url):
            try:
                
                metodo = item.h3.text.strip()
                descricao = item.p.text.strip()
                retorno = item.find('span', {'class': 'lightBlue'}).text
                exemplo_de_uso = item.find('pre', {'class': 'method-example-code'}).text.strip()
                resultado = {
                    metodo: {
                        'url': url,
                        'endpoint': url.replace('https://app.omie.com.br/api/v1/', ''),
                        'descricao': descricao,
                        'exemplo_de_uso': ast.literal_eval(exemplo_de_uso),
                        'retorno': retorno if retorno else ""
                        }
                    }
                dicionario_final.update(resultado)
                print(metodo, " -> ", retorno)
            except Exception as Error:
                print(metodo, "deu erro")

    return dicionario_final


def metodos():
    return pegar_todos_os_metodos([x for x in pega_links_api().values()])


def constroe_parametro(parametros: dict):
    codigo = ''
    for key, value in parametros.items():
        codigo += f'                "{key}":{value},\n'
    return '{\n' + codigo + '\n}'


def sanitiza_metodo(metodo: str) -> str:
    lista_palavras = re.sub(r"([A-Z])", r" \1", metodo).split()
    return ('_'.join(lista_palavras)).lower()


def gerar_codigo_automatico(dicionario: dict):
    
    def tratar_json(data: dict):
        return json.dumps(data, indent=4)
        
    
    codigo = 'from omieapi.core.omiebase import OmieBase \n\n' \
             '# Aviso -> antes de usar confira se não a oq vc precisa já feito no codigo principal,\n' \
             '# o codigo autogerdo pode conter erros não detectados ainda\n' \
             'class CodigoAutogerado(OmieBase):\n' \
             '  """ Este codigo foi automaticamente geredo por um script de scrap """'
    for metodo, valor in dicionario.items():

        lista_atributos = [x[0] for x in valor["exemplo_de_uso"].items()]
        param = dict(zip(lista_atributos, lista_atributos))

        codigo += \
            f'''\n    def {sanitiza_metodo(metodo)}(self, **kargs) -> dict:
                """ 
                {valor['descricao']} 
                :exemplo de uso:
                {tratar_json(valor['exemplo_de_uso'])}
                :link metodo: {valor['url']}
                :retorno:  {valor['retorno']}
                """
                return self._chamar_api(
                    call= '{metodo}',
                    endpoint= '{valor['endpoint']}',
                    param = kargs
                )
            '''
    with open('cod_automatico.py', 'w', encoding='utf-8') as w:
        w.write(codigo)


def gerar_codigo(metodos) -> None:
    gerar_codigo_automatico(metodos)


if __name__ == '__main__':
    gerar_codigo(metodos())
