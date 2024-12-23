# Um pequena analise de dados entendendo sobre as informações do nosso DataFrame

# Descomente o que for necessário
'''
    LEIA O MATEIRAL DE APOIO NA PASTA ANOTAÇÃO, SE SENTIR DIFICULDADES
    OU VEJAS OS CÓDIGOS DE EXEMPLOS
'''
import sys
import os

# criando diretório absoluto para adicionar a pasta pathpython com sys.path
# print(os.getcwd())

sys.path.append(os.path.abspath(os.path.join(os.getcwd())))

import pandas as pd
import numpy as np
from funcoes_curso.leitura_arquivo import leitura_arquivos_csv

# lendo e importando o nosso DataFrame
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_TermoAditivo.csv')
# essa função já retorna um DataFrame

# Retornar o tamnho da nossa base(linhas, colunas)
# print(df.shape) # saida -> (674, 10)

# Usando o Seletor head
# print(f'{df.head(2)}\n')

# Puxar informações das colunas que existem no nosso DataFrame
# print(df.info())

'''
SAIDA:
 #   Column                 Non-Null Count  Dtype 
---  ------                 --------------  ----- 
 0   Número Contrato        674 non-null    int64 
 1   Código Órgão Superior  674 non-null    int64 
 2   Nome Órgão Superior    674 non-null    object
 3   Código Órgão           674 non-null    int64 
 4   Nome Órgão             674 non-null    object
 5   Código UG              674 non-null    int64 
 6   Nome UG                674 non-null    object
 7   Número Termo Aditivo   674 non-null    int64 
 8   Data Publicação        667 non-null    object
 9   Objeto                 674 non-null    object
dtypes: int64(5), object(5)
memory usage: 52.8+ KB
'''
# Podemos Usar a função .describe() para descrever informações dtype dos dados das colunas
# o parâmetro include = tipo_dados, podemos sobre escrever o tipo de dado nesta coluna
# o parâmetro porcentiles, podemos usar para saber níveis de porcentagem de um determinado dado
# podemos colocar uma lista ou um objeto do python

# print(df.describe(percentiles= [0.1,0.2,0.3,0.4,0.5]))

# usando a função .sample() para puxar 5 linhdas de dados de colunas específicas

# index de colunas que vamos puxar com iloc =[0,1,8,9]

print(df.iloc[:,[0,1,8,9]].sample(n=5))