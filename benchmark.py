import timeit
from omieapi import Omie  # Supondo que o código anterior foi salvo como uma lib chamada `omie_lib`

# Configurações iniciais (chaves fictícias)
omie_app_key = input('sua_app_key: ')
omie_app_secret = input('seu_app_secreet: ')

# Parâmetros da chamada à API
metodo = "ListarContasCorrentes"
endpoint = "geral/contacorrente/"
parametros = {
    "pagina": 1,
    "registros_por_pagina": 100,
    "apenas_importado_api": "N"
}

# Função para o benchmark com requests sem sessão
def benchmark_requests_sem_sessao():
    omie = Omie(omie_app_key, omie_app_secret, session=False, use_httpx=False)
    return omie.conectar_api(metodo, endpoint, parametros)

# Função para o benchmark com httpx sem sessão
def benchmark_httpx_sem_sessao():
    omie = Omie(omie_app_key, omie_app_secret, session=False, use_httpx=True)
    return omie.conectar_api(metodo, endpoint, parametros)

# Função para o benchmark com requests com sessão
def benchmark_requests_com_sessao():
    with Omie(omie_app_key, omie_app_secret, session=True, use_httpx=False) as omie:
        return omie.conectar_api(metodo, endpoint, parametros)

# Função para o benchmark com httpx com sessão
def benchmark_httpx_com_sessao():
    with Omie(omie_app_key, omie_app_secret, session=True, use_httpx=True) as omie:
        return omie.conectar_api(metodo, endpoint, parametros)

runs = 2
# Função para medir o tempo de execução de cada teste
def run_benchmark():
    print("Benchmark: requests sem sessão")
    print(timeit.timeit(benchmark_requests_sem_sessao, number=runs))

    print("Benchmark: httpx sem sessão")
    print(timeit.timeit(benchmark_httpx_sem_sessao, number=runs))

    print("Benchmark: requests com sessão")
    print(timeit.timeit(benchmark_requests_com_sessao, number=runs))

    print("Benchmark: httpx com sessão")
    print(timeit.timeit(benchmark_httpx_com_sessao, number=runs))

if __name__ == "__main__":
    run_benchmark()
