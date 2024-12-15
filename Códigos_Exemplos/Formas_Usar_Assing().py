# FOI REIAPROVEITAR O CÓDIGO Adicionando_Colunas_em_Dataframe2.py
import sys
import os

# Adiciona o diretório base ao sys.path
# Estava dando erro aqui, copiei do chat, estude essa lib sys #copiei do código1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora os imports devem funcionar
import pandas as pd
import numpy as np
from datetime import time

# Com essas Funções podemos fazer leituras de arquivos excel e csv com libs
from funcoes_curso.leitura_arquivo import leitura_arquivos_excel, leitura_arquivos_csv
# As funções vão retornar um DataFrame
# Importando PandasGui para visualizarmos as colunas melhor
from pandasgui import show
''' 
    LEIA A ANOTAÇÃO: Abrindo_arquivos_com_lib1.txt
    LEIA A ANOTAÇÃO: Selecionando_colunas.txt
    LEIA A ANOTAÇÃO: A_importância_do_type()
    LEIA A ANOTAÇÃO: LOC_VS_ILOC.txt
    LEIA A ANOTAÇÃO: Manipulação_Colunas_DataFrame.txt
    LEIA A ANOTAÇÃO: Tratamento_dados1.txt
    LEIA A ANOTAÇÃO: Adicionando_Colunas_em_DataFrames1.txt
    LEIA A ANOTAÇÃO: Adicionando_Colunas_em_DataFrames2.txt
    LEIA A ANOTAÇÃO: Uso_do_.assing().txt
    VEJA O Código_Exemplo: data_frame4.py
    VEJA O Código_Exemplo: Adicionando_Colunas1.py
    VEJA O Código_Exemplo: Adicionando_Colunas2.py
'''
# Este é uma caso que podemos utilizar o PandasGui  para vizualizar melhor as coluans
# Vamos importar o PandasGui, Depos realizar Tratamento de dados para podermos trabalhar
# Com os dados das colunas e realizar o adicionamento de colunas usando .assing()

# Realizar tratamento das colunas Valor Inicial Compra, Valor Final Compra
# Estamos manipulando o DataFrame Original desta forma (diretamente)

# Criando o nosso DataFrame
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_Compras.csv')
#print(df.info()) # retorna informações sobre as colunas do DataFrame

# Definindo a lista de colunas que vamos Trabalhar
lista_colunas =['Valor Inicial Compra', 'Valor Final Compra']
# Exibindo a lista de colunas
print(df[lista_colunas[0:2]])
#print(type(df)) -> <class 'pandas.core.frame.DataFrame'>

# Usando a função applymap()
# Realizando tratamento de dados das colunas e convertendo para float
df[lista_colunas] = df[lista_colunas].applymap(lambda x: float(x.replace(',', '.')))

# Exibindo o DataFrame tratado
print(df[lista_colunas].info())

# criando função para adicionar coluna utilizando .assing()
def multiplicação_colunas_dataframe(df):
    return df['Valor Inicial Compra'] * df['Valor Final Compra']

# inserindo coluna com .assing()
'''
Lembre-se: parâmetro é o nome da coluna e o valor do parâmetro é o valor da coluna

 - Cada argumento de palavra-chave corresponde ao nome de uma nova:
    
    coluna e sua respectiva fórmula, lista, ou cálculo.

    Exemplo: assign(nova_coluna=lista, outra_coluna=fórmula)
            
    Nome da nova coluna -> seguido pelo valor ou fórmula que a define.
    Aceita listas, arrays, ou funções/lambdas que retornam colunas baseadas 
    no DataFrame.
'''

a = df.assign(Multiplicação_Colunas_com_def=multiplicação_colunas_dataframe(df)).loc[:,['Valor Inicial Compra', 'Valor Final Compra', 'Multiplicação_Colunas_com_def']]
print(f'{a}\n')

# Podemos Obter o mesmo resultado usando a função lambda

a = df.assign(Multiplicação_Colunas_com_lambda = lambda x: x['Valor Inicial Compra'] * x['Valor Final Compra'])
print(a.loc[0:5,['Valor Inicial Compra','Valor Final Compra','Multiplicação_Colunas_com_lambda']])

# Ao usar .assing() por padrão o pandaas faz uma copia do DataFrame Original
# isso ajudar a nos impedir de fazer cagadas