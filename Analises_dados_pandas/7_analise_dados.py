# importando libs
import sys
import os
import time
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


pasta_arquivo_csv = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'br_inep_ideb_brasil.csv')

print()
print(pasta_arquivo_csv)

df = pd.read_csv(pasta_arquivo_csv, encoding='utf - 8',)

#show(df)

# informando dados de todas as tabelas: 
print()
print(df.info())

'''
 1   rede                         126 non-null    object
 2   ensino                       126 non-null    object
 3   anos_escolares               126 non-null    object

'''

'''
ano int64
'''

colunas_object = ['rede', 'ensino', 'anos_escolares']

for colunas_category in colunas_object:
    df[colunas_category] = df[colunas_category].astype('category')
    
df['ano'] = df['ano'].astype(np.int16)


print()
print(df.info())
print()
print(df.memory_usage())


'''
 4   taxa_aprovacao               126 non-null    float64 
 5   indicador_rendimento         126 non-null    float64 
 6   nota_saeb_matematica         126 non-null    float64 
 7   nota_saeb_lingua_portuguesa  126 non-null    float64 
 8   nota_saeb_media_padronizada  126 non-null    float64 
 9   ideb                         126 non-null    float64 
 10  ...
'''

colunas_float64 = [ 'taxa_aprovacao' , 'indicador_rendimento', 'nota_saeb_matematica', 'nota_saeb_lingua_portuguesa', 'nota_saeb_media_padronizada', 'ideb', 'projecao']
for colunas_float32 in colunas_float64:
    df[colunas_float32] = df[colunas_float32].astype(np.float32)


print()
print(df.info())

print()
print(df.memory_usage())


print()
print(df['projecao'].isnull().sum()) # 28 dados null


# no final o uso de memória do DataFrame é memory usage: 4.6 KB

# Fazendo uma descrição geral das colunas, após o tratamento de dados

print(df.describe(include = 'all'))

'''
                ano      rede       ensino  ... nota_saeb_media_padronizada        ideb   projecao
count    126.000000       126          126  ...                  126.000000  126.000000  98.000000
unique          NaN         5            2  ...                         NaN         NaN        NaN
top             NaN  estadual  fundamental  ...                         NaN         NaN        NaN
freq            NaN        27           90  ...                         NaN         NaN        NaN
mean    2013.000000       NaN          NaN  ...                    5.243896    4.673810   4.744898
std        5.184593       NaN          NaN  ...                    0.804800    1.069443   1.134021
min     2005.000000       NaN          NaN  ...                    4.064600    3.000000   3.100000
25%     2009.000000       NaN          NaN  ...                    4.546586    3.800000   3.825000
50%     2013.000000       NaN          NaN  ...                    5.112608    4.500000   4.600000
75%     2017.000000       NaN          NaN  ...                    5.955065    5.600000   5.500000
max     2021.000000       NaN          NaN  ...                    7.184233    7.100000   7.400000


Veja !

count: O número de valores não nulos.
unique: O número de valores únicos.
top: O valor mais frequente (moda).
freq: A frequência do valor mais frequente.

'''

# tranformando o dataframe em um arquivo xlsx e movendo para pasta downloads

Arquivo_excel = df.to_excel("Inep_Ideb.xlsx", index = False)

try:
    caminho_origem = os.path.join(os.getcwd(),'Inep_Ideb.xlsx')
    print(f'\ncaminho de origem: {caminho_origem}\n')
    
    # usando a variável de ambiente USERPROFILE para montar 
    # um caminho na pasta DOWNLOADS
    pasta_downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')

    # caminho de trasferência para pasta downloads
    caminho_destino = os.path.join(pasta_downloads,'Inep_Ideb.xlsx')

    # Movendo o arquivo Excel, se existir
    if os.path.exists(caminho_origem):
        os.replace(caminho_origem, caminho_destino)
        print(f"Arquivo movido para: {caminho_destino}")
    else:
        print(f"Arquivo não encontrado em: {caminho_origem}\n")

except Exception as e:
    print(f'Aconteceu alguma cagada aqui: {e}')

# vizualizando dados com pandasgui
show(df)
