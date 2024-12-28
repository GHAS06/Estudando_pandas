# Aqui vamos fazer tudo o que fizemos antes, porém
# terá tratamento de dados, conversão do dataframe que possui dados tratados e modificados
# em arquivo excel, xlsx, 
# otimização de dados
# também terá manipulação de diretório 
# se possível usar a função concat()

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

df_csv = leitura_arquivos_csv('Arquivos_csv_estudos','202401_ItemCompra.csv')

print("Informações do nosso DataFrame:\n")
print(f'{df_csv.info()}\n')

# vizualizando o tanto de memória que o df_csv consome
print(f'{df_csv}\n')

# raalizando uma copia do dataframe para trabalharmos melhor
df_csv_copia = df_csv.copy(deep=True)
#print(df_csv_copia)

# Como os dados presentes neste dataframe, ele possui um certo nível de facilidade para 
# estourar o limite de armazenamento do dado, então vamos fazer uma boa análise
# exploratóra para selecionar as colunas que podem ter os dados reduzidos

# selecionando as colunas para converter de int64 para int32
colunas_int64 = [
    'Código Órgão','Código UG','Número Contrato','Quantidade Item'
]

for colunas_int32 in colunas_int64:
    df_csv_copia[colunas_int32] = df_csv_copia[colunas_int32].astype(np.int32)

print("Visualizando se as colunas foram modificadas: ")
print(f'\n{df_csv_copia.info()}')

# realizando conversão dos tipos object para category

# Realizando Tratmento de dados na coluna Valor Item, de object para float64

df_csv_copia['Valor Item'] = df_csv_copia.iloc[:,9].apply(lambda x: str(x.replace(',','.'))).astype(np.float64)

# Adicionando a coluna Valor Total Compra e manter o float64

df_csv_copia['Valor Total das Compras'] = (
        df_csv_copia['Quantidade Item'] * df_csv_copia['Valor Item']
    ).astype(np.float64)

# Vendo se a coluna foi adicionada
print(f'\n{df_csv_copia.info()}\n')

'''
# Tirei porque o consumo de memória estava maior que a anterior

try: 
    for col in df_csv_copia.columns: 

        col_tipo = df_csv_copia[col].dtypes 
        
        if col_tipo == "object":
            # Converter para category
            df_csv_copia[col] = df_csv_copia[col].astype("category")
except Exception as e:
    print(f"Olhe este erro: {e}")

# Vendo se as colunas Object foram mudadas para category
print(f'\n{df_csv_copia.info()}')

'''

#print(df_csv_copia.head())


# vamos converter nosso dataframe para um arquivo xlsx, se não possuir, converter
# para um csv e depois importar os dados do csv para o banco de dados
# é um projeto que iremos trabalhar no futuro

Arquivo_excel = df_csv_copia.to_excel("Compras_Governo.xlsx", index = False)

# vamos transferir o arquivo_excel para downloads, vamos reaproveitar código

try:
    caminho_origem = os.path.join(os.getcwd(),'Compras_Governo.xlsx')
    print(f'\ncaminho de origem: {caminho_origem}\n')
    
    # usando a variável de ambiente USERPROFILE para montar 
    # um caminho na pasta DOWNLOADS
    pasta_downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')

    # caminho de trasferência para pasta downloads
    caminho_destino = os.path.join(pasta_downloads,'Compras_Governo.xlsx')

    # Movendo o arquivo Excel, se existir
    if os.path.exists(caminho_origem):
        os.replace(caminho_origem, caminho_destino)
        print(f"Arquivo movido para: {caminho_destino}")
    else:
        print(f"Arquivo não encontrado em: {caminho_origem}\n")

except Exception as e:
    print(f'Aconteceu alguma cagada aqui: {e}')

# vizualizando com Pandasgui

show(df_csv_copia)