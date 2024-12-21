import sys
import os

# Adiciona o diretório base ao sys.path
# Estava dando erro aqui, copiei do chat, estude essa lib sys #copiei do código1

# Adiciona o diretório pai da pasta 'funcoes_curso' ao sys.path
sys.path.append(os.path.abspath('C:/Estudando_pandas_Copia'))

#Debugando
# Verifique se o diretório foi adicionado ao sys.path
#print(sys.path)

# Agora os imports devem funcionar
import pandas as pd
import numpy as np
from funcoes_curso.leitura_arquivo import leitura_arquivos_excel, leitura_arquivos_csv


# Aula de Seletores -> head, tail loc, sample

'''
    LEIA A ANOTAÇÃO: sys.txt
    LEIA A ANOTAÇÃO: os.txt
    LEIA A ANOTAÇÃO:
'''


df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_Compras.csv')

# usando o head() padrão
print()
print(df.head())
print()
# selecionando as 10 primeira linhas
print(df.head(10))
print()
# selecionando todas as linhas e colunas com o Seletor loc
print(df.loc[:,:]) # saida -> 3810 rows x 24 columns
print()
# reduzindo a quntidade de linhas no head()
print(df.head(-3500)) # retornou 310 rows x 24 columns do nosso DataFrame
print()
# retornando nem uma linha com head()
print(df.head(-3810)) # saida -> Empty DataFrame, porém retora todas as nossas colunas
print(type(df.head(-3810))) # é de fato um DataFrame
print()