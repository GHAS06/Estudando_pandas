import sys
import os

# Adiciona o diretório base ao sys.path
# Estava dando erro aqui, copiei do chat, estude essa lib sys #copiei do código1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# esses .. representa que está subiindo um nível na hierarquia dos módulos
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
    VEJA O Código_Exemplo: data_frame4.py
    VEJA O Código_Exemplo: Adicionando_Colunas1.py
'''
 
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_Compras.csv')

#print(df.info()) # retorna informações sobre as colunas do DataFrame
'''
Saida: 
 0   Número do Contrato                  3810 non-null   int64
 1   Objeto                              3810 non-null   object
 2   Fundamento Legal                    25 non-null     object
 3   Modalidade Compra                   3810 non-null   object
 4   Situação Contrato                   3810 non-null   object
 5   Código Órgão Superior               3810 non-null   int64
 6   Nome Órgão Superior                 3810 non-null   object
 7   Código Órgão                        3810 non-null   int64
 8   Nome Órgão                          3810 non-null   object
 9   Código UG                           3810 non-null   int64
 10  Nome UG                             3810 non-null   object
 11  Data Assinatura Contrato            3810 non-null   object
 12  Data Publicação DOU                 3810 non-null   object
 13  Data Início Vigência                3810 non-null   object
 14  Data Fim Vigência                   3773 non-null   object
 15  Código Contratado                   3810 non-null   object
 16  Nome Contratado                     3810 non-null   object
 17  Valor Inicial Compra                3810 non-null   object
 18  Valor Final Compra                  3810 non-null   object
 19  Número Licitação                    3810 non-null   int64
 20  Código UG Licitação                 2880 non-null   float64
 21  Nome UG Licitação                   2880 non-null   object
 22  Código Modalidade Compra Licitação  2880 non-null   float64
 23  Modalidade Compra Licitação         2880 non-null   object
'''
# Este é uma caso que podemos utilizar o PandasGui  para vizualizar melhor as coluans
# Vamos importar o PandasGui, Depos realizar Tratamento de dados para podermos trabalhar
# Com os dados das colunas e realizar o adicionamento de colunas usando diferentes formas

# Realizar tratamento das colunas Valor Inicial Compra, Valor Final Compra
# Estamos manipulando o DataFrame Original desta forma (diretamente)

# Definindo a lista de colunas que vamos Trabalhar
lista_colunas =['Valor Inicial Compra', 'Valor Final Compra']
# Exibindo a lista de colunas
print(df[lista_colunas[0:1]])
#print(type(df)) -> <class 'pandas.core.frame.DataFrame'>

# Usando a função applymap()
# Realizando tratamento de dados das colunas e convertendo para float
df[lista_colunas] = df[lista_colunas].applymap(lambda x: float(x.replace(',', '.')))

# Exibindo o DataFrame tratado
print(df[lista_colunas].info()) 
'''
 0   Valor Inicial Compra  3810 non-null   float64
 1   Valor Final Compra    3810 non-null   float64
'''
#print(df.info())
'''
 0   Número do Contrato                  3810 non-null   int64
 1   Objeto                              3810 non-null   object
 2   Fundamento Legal                    25 non-null     object
 3   Modalidade Compra                   3810 non-null   object
 4   Situação Contrato                   3810 non-null   object
 5   Código Órgão Superior               3810 non-null   int64
 6   Nome Órgão Superior                 3810 non-null   object
 7   Código Órgão                        3810 non-null   int64
 8   Nome Órgão                          3810 non-null   object
 9   Código UG                           3810 non-null   int64
 10  Nome UG                             3810 non-null   object
 11  Data Assinatura Contrato            3810 non-null   object
 12  Data Publicação DOU                 3810 non-null   object
 13  Data Início Vigência                3810 non-null   object
 14  Data Fim Vigência                   3773 non-null   object
 15  Código Contratado                   3810 non-null   object
 16  Nome Contratado                     3810 non-null   object
 17  Valor Inicial Compra                3810 non-null   float64
 18  Valor Final Compra                  3810 non-null   float64
 19  Número Licitação                    3810 non-null   int64
 20  Código UG Licitação                 2880 non-null   float64
 21  Nome UG Licitação                   2880 non-null   object
 22  Código Modalidade Compra Licitação  2880 non-null   float64
 23  Modalidade Compra Licitação         2880 non-null   object

Veja que o tipo de dado foi modificado!
'''
# Armazenando a média aritimética com a função .mean() de uma coluna e armazendo em uma variável
# usando a função insert para adcionar uma coluna em uma posição específica

média_v_inicial = df.loc[:,'Valor Inicial Compra'].mean()
df.insert(18,'Média Valor Compra Inicial', média_v_inicial )
print(df.info())
# Essa média da compra inicial vai aparecer em todas as linhas, é literalmente a média
# de todos os valores que estão na coluna Valor Compra Inicial

# Vamos Reaproveitar o código para a média do Valor Final Compra

média_v_final = df.loc[:,'Valor Final Compra'].mean()
df.insert(20,'Média Valor Final Compra', média_v_final )
print(df.info())

# A mesma situação da média se aplica aqui
'''
0   Número do Contrato                  3810 non-null   int64
 1   Objeto                              3810 non-null   object
 2   Fundamento Legal                    25 non-null     object
 3   Modalidade Compra                   3810 non-null   object
 4   Situação Contrato                   3810 non-null   object
 5   Código Órgão Superior               3810 non-null   int64
 6   Nome Órgão Superior                 3810 non-null   object
 7   Código Órgão                        3810 non-null   int64
 8   Nome Órgão                          3810 non-null   object
 9   Código UG                           3810 non-null   int64
 10  Nome UG                             3810 non-null   object
 11  Data Assinatura Contrato            3810 non-null   object
 12  Data Publicação DOU                 3810 non-null   object
 13  Data Início Vigência                3810 non-null   object
 14  Data Fim Vigência                   3773 non-null   object
 15  Código Contratado                   3810 non-null   object
 16  Nome Contratado                     3810 non-null   object
 17  Valor Inicial Compra                3810 non-null   float64
 18  Média Valor Compra Inicial          3810 non-null   float64
 19  Valor Final Compra                  3810 non-null   float64
 20  Média Valor Final Compra            3810 non-null   float64
 21  Número Licitação                    3810 non-null   int64
 22  Código UG Licitação                 2880 non-null   float64
 23  Nome UG Licitação                   2880 non-null   object
 24  Código Modalidade Compra Licitação  2880 non-null   float64
 25  Modalidade Compra Licitação         2880 non-null   object

Veja! As colunas foram adcionadas no nosso DataFrame Original, Recomendo fazer isso
com Atenção.
'''

# Agora Vamos Usar o PandasGui para Visualizar os dados
show(df)