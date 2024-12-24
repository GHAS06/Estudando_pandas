# Continuando com a analise exploratório, parte 2
# nível intermediário para avançado
# com arquivo diferente
# Vamos usar as funções:
# usar os métodos anterior na parte 1
# select_dtypes(include = [lista de dados que estamos selecionando]) 
# usar também o método type(), .isnull(), .unique()
# usar função para visualizarmos consumo de memória .memory_usage(deep = True)
# usar o pandasgui para visualizar dados possíveis de modificação

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
        
from funcoes_curso.leitura_arquivo import leitura_arquivos_csv

# selecionando as cinco primeiras linhas do DataFrame
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_TermoAditivo.csv')
print(f"{df.head()}\n")

# usando a função info() para puxar informações das colunas do DataFrame
print(f'{df.info()}')

# Usando o dtypes() para  puxar informações dos tipos_de_dados dos dados das colunas 
print(f'\n{df.dtypes}')

# puxando indormações estátisticas de todas as colunas e seus tipos de dados
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
<class 'NoneType'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.series.Series'>
'''

# Usou de memória que o DataFrame consome

print(f'\n{df.memory_usage(deep= True)}\n')

# Selecionando colunas com tipo de dados específicos com select_dtypes([lista_tipo_dados])

df.select_dtypes(['object'])

# fazendo uma conversão de tipo de dados, de objetc para category nesta coluna com tipo
# de dado object

print("Aqui está as colunas  com dados object:")

print(f'\n{df.select_dtypes("object")}')


df['Nome Órgão Superior'] = df['Nome Órgão Superior'].astype('category')
df['Nome Órgão'] = df['Nome Órgão'].astype('category')
df['Nome UG'] = df['Nome UG'].astype('category')
df['Data Publicação'] = df['Data Publicação'].astype('category')
df['Objeto'] = df['Objeto'].astype('category')

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
print(df['Objeto'].unique())
# basicamente o .unique() faz a mesma coisa que o .nunique(), porém retorna
# um array de valores únicos.

# usando o pandasgui
#show(df)

# visualizei possíveis dados nulos em Data Publicação

# Realizando um filtro para contabilizar todos os valores que são nulos desta coluna
print('Essa bagaceira:\n')
print(df.isnull().sum())

# a maneira correta de contabilizar valores nulos é usar o .sum()
# Veja, apenas Data Publicação retorna valores nulos e são 7
# não conte com .count() para contabilizar valores nulos, ele ignonra isso