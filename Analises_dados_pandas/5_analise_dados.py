# Continuando com a analise de dados essa é a parte 3
# Nível avançado
# vamos usar outro arquivo csv
# Vamos usar as funções: .loc() ou iloc()
# para selecionar colunas
# com base na vizualização dos dados anteriores:
# usaremos vetores_lógicos para retornar um series dos dados candidatos para modificação
# usar a função .copy() para realizar uma copia do dataframe não fazer cagada no original
# usaremos .mamory_usage(deep = True) para realizar gerencimento de memória
# também iremos usar a função .apply() para modificar dados de colunas específicas
# ou iremos usar a função .applymap() para modificar dataframe em uma coluna específica


# importando libs
import sys
import os
import requests 
import pandas as pd
import numpy as np
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
        
from funcoes_curso.leitura_arquivo import leitura_arquivos_csv

# selecionando as cinco primeiras linhas do DataFrame
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_ItemCompra.csv')
print(f"{df.head()}\n")

# usando a função info() para puxar informações das colunas do DataFrame
print(f'{df.info()}')

# Usando o dtypes() para  puxar informações dos tipos_de_dados dos dados das colunas 
print(f'\n{df.dtypes}')

# puxando informações estátisticas de todas as colunas e seus tipos de dados
print(f'\n{df.describe(include="all")}')

# contabilizando os valores unicos com nunique.
print(f'\n{df.nunique()}\n')

# Entendendo cada saida com type()

print(type(df.head()))
print(type(df.info()))
print(type(df.dtypes))
print(type(df.describe(include='all')))
print(type(df.nunique()))

# Saidas com Type
'''
<class 'pandas.core.frame.DataFrame'>
<class 'NoneType'> aqui sempre vai retomar Nonetype por padrão
<class 'pandas.core.series.Series'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.series.Series'>
'''

# Usou de memória que o DataFrame consome

print(f'\n{df.memory_usage(deep= True)}\n')

# Selecionando colunas com tipo de dados específicos com select_dtypes([lista_tipo_dados])

df.select_dtypes(['int64'])

# fazendo uma conversão de tipo de dados, de int64 para int8 ou float 16 nas colunas
# com tipo de dado int64

print("Aqui está as colunas com dados int64 convertido para int32, float 16: ")

print(f'\n{df.select_dtypes("int64","float16").astype(np.int32)}')

# usando for passando uma lista de colunas para modificar o tipo de dados de várias
# colunas de uma vez
colunas_para_converter = ['Código Órgão', 'Código UG', 'Número Contrato', 'Quantidade Item']
for coluna in colunas_para_converter:
    df[coluna] = df[coluna].astype(np.int32)

df['Valor Item'] = df.iloc[:,9].apply(lambda x: str(x.replace(',','.'))).astype(np.float16)

# Adicinando coluna Valor Total Compra

df['Valor Total Compra'] = (df['Quantidade Item'] * df['Valor Item']).astype(np.float32)

# vizualizando se as colunas foram modificadas com .info()
print(f'\n{df.info()}')

# Visualizando se essa conversão de dados reduziu o consumo de memória
print(f'\n{df.memory_usage(deep = True)}\n')
# o uso de memória fez foi aumentar

# checando se todas as colunas possuem valores null ou NaN

print(df[df.iloc[:,:] == 'NaN'].describe())
# acabamos de constatar que não existem valores nullos aqui, pois o .isnull()
# retorna um series ou um dataframe, depende como você está manipulandos os dados no pandas
# com valores booleanos, True ou False
# Certo? Errado! o count, ignora se os valores são nulos, ele também contabiliza valores
# nulos, ou seja, ele contabiliza o total de linhas que contém essa coluna do DataFrame


# .unique só é usado em serie, já o .nunique() é usado em DataFrames
print()
print(df['Nome Órgão'].unique())
# basicamente o .unique() faz a mesma coisa que o .nunique(), porém retorna
# um array de valores únicos.

# Realizando um filtro para contabilizar todos os valores que são nulos desta coluna
print('\nEssa bagaceira:\n')
print(df.isnull().sum())

# a maneira correta de contabilizar valores nulos é usar o .sum()
# Veja, neste arquivo.csv nem uma coluna possui 
# não conte com .count() para contabilizar valores nulos, ele ignonra isso

# Por mais que já tenha feito as modificações sem a função .copy()
# nada de errado aconteceu, agora vamos usá-la para previnir cagadas

df_copia = df.copy(deep = True)

# retornando os cincos primeiros dados do dataframe copiado
print(f'\n{df_copia.head()}')

# usando operadores_lógicos para retornar vetores lógicos e realizar filtros e
# e usando o pandasgui para ter melhor visualização de dados

show(df[(df['Nome Órgão'] == 'Comando do Exército') & (df['Valor Total Compra'] >= 100000)])

# Veja que foi retornado dados inf que significa infinito, isso acontece porque o dado
# ultrapassa o limite de armazenamento, se ele é float32 e está como info o  certo a 
# fazer é voltar para 64 bit (float64)