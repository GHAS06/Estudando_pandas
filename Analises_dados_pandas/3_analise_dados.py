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
        
from funcoes_curso.leitura_arquivo import leitura_arquivos_excel

# Objetivo aqui é fazer uma análise exploratório, parte 1
# Nível básico

# vamos usar as funções: .nunique(), .describe(include = 'all'), .info(), .dtypes()
# usar também o método type()

# selecionando as cinco primeiras linhas do DataFrame
df = leitura_arquivos_excel('Arquivos_excel_para_estudos','Vendas.xlsx')
print(f"{df.head(5)}\n")

# usando a função info() para puxar informações das colunas do DataFrame
print(f'{df.info()}')

# Usando o dtypes() para  puxar informações dos tipos_de_dados dos dados das colunas 
print(f'\n{df.dtypes}')

# puxando indormações estátisticas de todas as colunas e seus tipos de dados
print(f'\n{df.describe(include= "all")}')

# contabilizando os valores unicos com nunique.
print(f'\n{df.nunique()}')

# Entendendo cada saida com type()

print(type(df.head(5)))
print(type(df.info()))
print(type(df.dtypes))
print(type(df.describe(include='all')))
print(type(df.nunique()))

# Saidas com Type
'''
<class 'pandas.core.frame.DataFrame'>
<class 'NoneType'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.series.Series'>
'''