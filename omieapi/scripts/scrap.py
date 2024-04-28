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

def retorna_tipos_complexos(url: str):
    def request_omieapi(url: str) -> BeautifulSoup:
        try:
            r = get(url, headers={'Content-type': 'text/html; charset=UTF-8'})
            r.raise_for_status()
            return BeautifulSoup(r.text, features="html.parser")
        except:
            raise Exception('Erro na requisição')
    soap = request_omieapi(url)
    return soap.find_all('div', {'class': 'complexTypeItem'})
    
    

def pegar_todos_os_metodos(urls: list[str]):
    
    def pegar_descricao(item) -> str | None:
        try:
            return item.p.text.strip()
        except:
            return None
                
    def pegar_retorno(item):
        try:
            return item.find('span', {'class': 'lightBlue'}).text
        except:
            return None
        
    acerto_erro = [0, 0]
    dicionario_final = {}
    for url in urls:
        for item in retorna_divs_de_metodos(url):
            try:
                metodo = item.h3.text.strip()
                descricao = pegar_descricao(item) if pegar_descricao(item) else ""
                retorno = pegar_retorno(item) if pegar_retorno(item) else ""
                exemplo_de_uso = item.find('pre', {'class': 'method-example-code'}).text.strip()
                resultado = {
                    metodo: {
                        'url': url,
                        'endpoint': url.replace('https://app.omie.com.br/api/v1/', ''),
                        'descricao': descricao,
                        'exemplo_de_uso': ast.literal_eval(exemplo_de_uso.replace("false", "False").replace("true", "True")),
                        'retorno': retorno if retorno else ""
                        }
                    }
                dicionario_final.update(resultado)
                acerto_erro[0] += 1
                print("\033[92m", metodo, " -> ", retorno)
            except Exception as Error:
                print("\033[91m", metodo, "deu erro", Error)
                acerto_erro[1] += 1
        print("\033[90m", f"Concluidos e Falhas {acerto_erro}")

    print("\033[90m", f"Concluidos e Falhas {acerto_erro}")
    return dicionario_final


def metodos():
    return pegar_todos_os_metodos([x for x in pega_links_api().values()])

def tipos():
    return pega_todos_tipos_complexos([x for x in pega_links_api().values()])

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
        return json.dumps(data, indent=16).replace("}", '').replace("{", '')
        
    
    codigo = 'from omieapi.core.omiebase import OmieBase \n\n' \
             '# Aviso -> antes de usar confira se não a oq vc precisa já feito no codigo principal,\n' \
             '# o codigo autogerdo pode conter erros não detectados ainda\n' \
             'class CodigoAutogerado(OmieBase):\n'\
             '  """ Este codigo foi automaticamente geredo por um script de scrap """'
    for metodo, valor in dicionario.items():

        lista_atributos = [x[0] for x in valor["exemplo_de_uso"].items()]
        param = dict(zip(lista_atributos, lista_atributos))

        codigo += \
            f'''\n    def {sanitiza_metodo(metodo)}(self, **kargs) -> dict:
                """ 
                {valor['descricao']} 
                :exemplo de uso:
                {"{"}
                {tratar_json(valor['exemplo_de_uso'])}
                {"}"}
                
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

def pega_todos_tipos_complexos(urls: list[str]) -> list:

    remove_numero = lambda x: ''.join([i for i in x if not i.isdigit()])

    lista_tipos: list = []

    for url in urls:
        for item in retorna_tipos_complexos(url):
            parametros = []
            try:
                nome = item.h3.text
                descricao = item.p.text

                for parametro in item.table.find_all("tr"):

                    nome_parametro = parametro.find("td", {"class": "parameter-name"})
                    tipo = parametro.find("td", {"class": "parameter-type"})
                    descricao_parametro = parametro.find("td", {"class": "parameter-docs"})
                    parametros.append(
                        {
                            "nome_parametro": nome_parametro.text if nome_parametro else "",
                            "tipo_parametro": remove_numero(tipo.text) if tipo else "None",
                            "descricao_parametro": descricao_parametro.text if descricao_parametro else ""
                        }
                    )

                lista_tipos.append(
                    {
                        "nome": nome,
                        "descricao": descricao,
                        "parametros": parametros
                    }
                )

            except Exception as error:
                print(error)
    print("Fim acabou")
    print(lista_tipos)
    return lista_tipos

def gerar_codigo_automatico_php(dicionario: dict):

    def lower_first_letter(string) -> str:
        if len(string) > 0:
            return string[0].lower() + string[1:]
        else:
            return string
        
    def sanitiza_metodo_php(metodo: str) -> str:
        lista_palavras = re.sub(r"([A-Z])", r" \1", metodo).split()
        nome_final = ''.join(lista_palavras)
        return lower_first_letter(nome_final)

    codigo = '<?php\n' \
             'include(omieBase.php); \n\n' \
             'class OmieAuto extends OmieBase{\n'
    for metodo, valor in dicionario.items():

        lista_atributos = [x[0] for x in valor["exemplo_de_uso"].items()]
        param = dict(zip(lista_atributos, lista_atributos))
        codigo += \
            f'''\n    public function {sanitiza_metodo_php(metodo)}(array $parametros): array {"{"} 
                    //{valor['descricao']} 
                    return $this->chamarApi(
                        "{valor['endpoint']}",
                        "{metodo}",
                        $parametros
                    );
            {"}"}
                '''
    codigo += "\n}"
    with open('php/omieAuto.php', 'w', encoding='utf-8') as w:
        w.write(codigo)


def gerar_codigo_automatico_java(dicionario: dict):

    def lower_first_letter(string) -> str:
        if len(string) > 0:
            return string[0].lower() + string[1:]
        else:
            return string
    def sanitiza_metodo_java(metodo: str) -> str:
        lista_palavras = re.sub(r"([A-Z])", r" \1", metodo).split()
        nome_final = ''.join(lista_palavras)
        return lower_first_letter(nome_final)

    def tratar_json(data: dict):
        return json.dumps(data, indent=16).replace("}", '').replace("{", '')


    codigo = 'package org; \n\n' \
             'import org.json.JSONObject;\n' \
             'import java.io.IOException;\n' \
             'import java.net.URISyntaxException;\n\n' \
             'public class OmieAuto extends OmieObject{\n' \
             '    public OmieAuto(String appKey, String appSecreet) {\n' \
             '    super(appKey, appSecreet);\n' \
             '}\n'
    for metodo, valor in dicionario.items():

        lista_atributos = [x[0] for x in valor["exemplo_de_uso"].items()]
        param = dict(zip(lista_atributos, lista_atributos))
        codigo += \
            f'''\n    public JSONObject {sanitiza_metodo_java(metodo)}(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException{"{"} 
                    //{valor['descricao']} 
    
                    return this.chamarApi(
                        "{valor['endpoint']}",
                        "{metodo}",
                        parametros
                    );
            {"}"}
                '''
    codigo += "\n}"
    with open('java/apiomie/src/main/java/org/OmieAuto.java', 'w', encoding='utf-8') as w:
        w.write(codigo)

def gerar_codigo(metodos) -> None:
    gerar_codigo_automatico(metodos)

def gerar_codigo_java(metodos) -> None:
    gerar_codigo_automatico_java(metodos)

def gerar_codigo_tipos_automatico_em_python(lista_tipos: list):
    codigo = 'from dataclasses import dataclass \n\n' \
             '# Aviso -> antes de usar confira se não a oq vc precisa já feito no codigo principal,\n' \
             '# o codigo autogerdo pode conter erros não detectados ainda\n\n'
    for tipo in lista_tipos:
        codigo += f'''@dataclass\nclass {tipo["nome"]}:\n    """{tipo["descricao"]}"""\n'''

        for parametro in tipo['parametros']:
            codigo += f'    {parametro["nome_parametro"]} #{parametro["tipo_parametro"]}\n'

    with open('tipos_complexos.py', 'w', encoding='utf-8') as w:
        w.write(codigo)

if __name__ == '__main__':
    #gerar_codigo(metodos())
    #gerar_codigo_automatico_java(metodos())
    #gerar_codigo_automatico_php(metodos())
    #gerar_codigo_tipos_automatico_em_python(tipos())
    ...