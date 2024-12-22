# importando libs
import sys
import os
import time
import requests 
import pandas as pd
from pandasgui import show

try:
    # realizando testes para saber qual diretório estou
    print(os.getcwd())

    # fazendo um caminho absoluto para o interpretador python ler
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # puxando o ultimo item da lista de módulos lida pelo interpretador
    print(sys.path[-1])

except Exception as e:
    print(f"Erro: {e}")

from funcoes_curso.pokemon_api_dados import dados_pokemon

try:
    # puxando o DataFrame da API do Pokemon
    DataFrame = dados_pokemon()
    # Transformando o DataFrame em um aquivo excel
    print("\nProcessendo Aquivo excel")
    time.sleep(5)
    DataFrame.to_excel('Excel_Pokemons.xlsx', index=False)
    print("\nArquivo Excel criado com sucesso.\n")
except Exception as e:
    print(f"Erro ao criar o arquivo Excel: {e}")

# montando automação de diretórios
try:
    caminho_origem = os.path.join(os.getcwd(),'Excel_Pokemons.xlsx')
    print(f'\ncaminho de origem: {caminho_origem}\n')
    
    # reaproveitando código, usando a variável de ambiente USERPROFILE para montar 
    # um caminho na pasta DOWNLOADS
    pasta_downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')

    # caminho de trasferência para pasta downloads
    caminho_destino = os.path.join(pasta_downloads,'Excel_Pokemons.xlsx')

    # Movendo o arquivo Excel, se existir
    if os.path.exists(caminho_origem):
        os.replace(caminho_origem, caminho_destino)
        print(f"Arquivo movido para: {caminho_destino}")
    else:
        print(f"Arquivo não encontrado em: {caminho_origem}")

except Exception as e:
    print(f'Aconteceu alguma cagada aqui: {e}')

# Usando PandasGui para analisar dados
show(DataFrema)
