import sys
import os

# Adiciona o diretório base ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
from funcoes_curso.leitura_arquivo import leitura_arquivos_csv

'''
                        RECOMENDAÇÃO:

    LEIA A ANOTAÇÃO: Conversão_de_memória.txt
    LEIA A ANOTAÇÃO: Otimização_Uso_Memória.txt
    LEIA A ANOTAÇÃO: Copia_Dados_Pndas.txt
'''

# Essa função vai retornar um DataFrame a partir de um arquivo csv
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_Compras.csv')
# verificando o Dataframe
print(df.head())

# puxando informações dos dados dasdas colunas do DataFrame com .info()
print(df.info())    
'''
SAIDA:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3810 entries, 0 to 3809
    Data columns (total 24 columns):
    #   Column                              Non-Null Count  Dtype
    ---  ------                              --------------  -----
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
    dtypes: float64(2), int64(5), object(17)
    memory usage: 714.5+ KB

Veja! Possuimos informações completas do DataFrame, desde o tipo de dados do DataFrame
até o uso me memória em memory usage: 714.5+
'''

# RECOMENDAÇÃO: SEMPRE QUE POSSÍVEL, QUANDO TRABALHAR COM BASE DE DADOS MUITO GRANDE
# USE O MÉTODO .copy() PARA REALIZAR UM COPIA  DESTA BASE DE DADOS, ASSIM EVITAMOS 
# CAGADAS AO REALIZAR A ANÁLISE DE DADOS

# puxando informações dos dados com o atributo dtypes, das colunas
print(df.dtypes)

'''
SAIDA:
    Número do Contrato                      int64
    Objeto                                 object
    Fundamento Legal                       object
    Modalidade Compra                      object
    Situação Contrato                      object
    Código Órgão Superior                   int64
    Nome Órgão Superior                    object
    Código Órgão                            int64
    Nome Órgão                             object
    Código UG                               int64
    Nome UG                                object
    Data Assinatura Contrato               object
    Data Publicação DOU                    object
    Data Início Vigência                   object
    Data Fim Vigência                      object
    Código Contratado                      object
    Nome Contratado                        object
    Valor Inicial Compra                   object
    Valor Final Compra                     object
    Número Licitação                        int64
    Código UG Licitação                   float64
    Nome UG Licitação                      object
    Código Modalidade Compra Licitação    float64
    Modalidade Compra Licitação            object
    dtype: object

Veja! Basicamente pegamos as mesmas informações acima, porém mais enxuto, no caso, apenas 
colunas e seus respectivos tipos de dados
'''

# Verificando o uso de memória com o método .memory_usage(), é propria do DataFrame.

print(df.memory_usage(deep = True))
'''
SAIDA:
    Index                                     132
    Número do Contrato                      30480
    Objeto                                1173708
    Fundamento Legal                       124184
    Modalidade Compra                      374450
    Situação Contrato                      357394
    Código Órgão Superior                   30480
    Nome Órgão Superior                    401806
    Código Órgão                            30480
    Nome Órgão                             402553
    Código UG                               30480
    Nome UG                                363746
    Data Assinatura Contrato               255270
    Data Publicação DOU                    255270
    Data Início Vigência                   255270
    Data Fim Vigência                      253975
    Código Contratado                      268740
    Nome Contratado                        355623
    Valor Inicial Compra                   257641
    Valor Final Compra                     257621
    Número Licitação                        30480
    Código UG Licitação                     30480
    Nome UG Licitação                      301057
    Código Modalidade Compra Licitação      30480
    Modalidade Compra Licitação            315716
    dtype: int64

Sobre o método: 
    
    é usado para verificar a quantidade de memória ocupada por um DataFrame ou por suas
    colunas. É uma ferramenta poderosa para monitorar e otimizar o consumo de memória,
    especialmente ao trabalhar com grandes conjuntos de dados.

Sintaxe: 

    DataFrame.memory_usage(index=True, deep=False)

Parâmetros:
    
    - index (bool, padrão: True): Indica se o tamanho da memória do índice deve ser incluído na análise.
        
        Se True, o uso de memória do índice será exibido.
        Se False, apenas as colunas serão consideradas.

    - deep (bool, padrão: False):

    Quando True, o Pandas calcula o uso de memória mais detalhado, especialmente para
    objetos como strings ou categorias.
    
    Quando False, fornece uma estimativa superficial (mas mais rápida).

Retorno: 

    Um objeto Series que contém o uso de memória (em bytes) para cada coluna do DataFrame,
    incluindo opcionalmente o índice.

'''
# Realizando uma copia do dataframe com .copy()

df_copia = df.copy(deep=True)
print() # apenas para pular uma linha
print(df_copia.head()) # copia realizada com sucesso!

# usando a função/método .astype(tipo_de_dados) para convertar dados de colunas específicas

'''
    Vamos modificar o tipo de dados das colunas Valor Inicial Compra, Valor Final Compra
    elas estão como object, e vai passar a ser int8 (np.int8)
'''
print()#quebra de linha
df_copia['Valor Inicial Compra'] = df_copia['Valor Inicial Compra'].str.replace(',','.').astype(np.float16)
print(type(df_copia['Valor Inicial Compra'][0]))
# saida <class 'numpy.float16'>

# Reaproveitar o código para fazer a conversão no Valor Final Compra
print()#quebra de linha
df_copia['Valor Final Compra'] = df_copia['Valor Final Compra'].str.replace(',','.').astype(np.float16)
print(type(df_copia['Valor Final Compra'][0]))
print() # só para quebra de linha

# Puxando as dua colunas para retornar DataFrame
print(df_copia.loc[0:4,['Valor Inicial Compra', 'Valor Final Compra']])
print((type(df_copia[['Valor Inicial Compra', 'Valor Final Compra']])))
# saidaa <class 'pandas.core.frame.DataFrame'>

# float16 não é tão bem aceito pelo DataFrame, retorna valores inf

# Verificando o Uso de memória
print()
print(df_copia.memory_usage(deep=True))
print()

'''
SAIDA:
    
    df:
        
        Valor Inicial Compra                   257641
        Valor Final Compra                     257621

    df_copia: 

    Valor Inicial Compra                     7620
    Valor Final Compra                       7620

    Veja que reduzimos bastante o uso de memória das colunas acima, lembrando que é 
    calculado em bytes
'''

# Usando o método .nunique()

'''
    O método .nunique() do Pandas é usado para contar o número de valores únicos em uma 
    coluna ou DataFrame. Ele pode ser muito útil para entender a diversidade de dados em
    um conjunto e para verificar a quantidade de categorias ou valores diferentes em uma
    variável.

    - Para que serve o método .nunique()?

        O .nunique() é útil quando você deseja:

         - Contar os valores distintos em uma coluna de dados.
         - Verificar a diversidade de categorias ou valores em um conjunto de dados.
         - Analisar variáveis que possuem poucos ou muitos valores únicos 
         (ex: categorias de produtos, faixas etárias, etc.).

    Sintaxe:
        
        DataFrame.nunique(axis=0, dropna=True)
    
    Parâmetros:
    
        axis: Determina se o cálculo será feito nas colunas (default) ou nas linhas.
        axis=0 (default): Conta os valores únicos em cada coluna.
        axis=1: Conta os valores únicos em cada linha.
        dropna: Determina se valores NaN (ausentes) devem ser ignorados.
        dropna=True (default): Ignora valores ausentes.
        dropna=False: Conta os valores NaN como uma categoria única.

    Resumo:

        - O método .nunique() conta o número de valores únicos em uma coluna ou DataFrame.
        - Pode ser usado para entender a diversidade de dados e analisar a quantidade de
        categorias diferentes.
        - Você pode escolher se quer ignorar ou contar os valores ausentes (NaN), e também
        pode contar valores únicos ao longo das linhas, se necessário.
'''

#Filtrar o DataFrame para contar os valores únicos apenas nas colunas que possuem tipos de dados 'object', 'int64' ou 'float16'
print(df_copia.select_dtypes(include = ['object', 'int64','float16']).nunique())

# passando alguns dados para 'category'

df_copia['Código Contratado'] = df['Código Contratado'].astype('category')
df_copia['Nome Contratado'] = df['Nome Contratado'].astype('category')
df_copia['Valor Inicial Compra'] = df['Valor Inicial Compra'].astype('category')
df_copia['Valor Final Compra'] = df['Valor Final Compra'].astype('category')

'''
Por que usar o tipo category?
    
    Otimização de memória: O tipo category é particularmente útil quando você tem uma
    coluna com um número limitado de valores únicos, mas com um grande número 
    de observações (ou seja, valores repetidos). Isso pode ser muito mais eficiente em
    termos de memória, já que em vez de armazenar o valor completo para cada linha
    (como uma string, por exemplo), o Pandas armazena um índice numérico para cada valor
    único.

    Quando você converte uma coluna para o tipo category, o Pandas cria um dicionário
    interno que mapeia os valores únicos da coluna para números inteiros
    (e internamente mantém o valor original mapeado para esses inteiros).
    Isso reduz o espaço de memória consumido, especialmente se a coluna contiver muitas
    repetições de um número pequeno de valores distintos.

    Internamente, o Pandas agora representa os valores dessa coluna usando um índice
    numérico, economizando memória, especialmente se o número de valores únicos for
    pequeno em relação ao número total de entradas.
'''

# comparando o uso de memoria:
print(df_copia.memory_usage(deep = True))
# usar o category ficou muito maior que o float64

# fazendo um calculo matemático
df_comparação = (df_copia.memory_usage(deep = True)/df.memory_usage(deep = True)) 
print()
print(df_comparação)

'''
SAIDA:
 
    Index                                 1.000000
    Número do Contrato                    1.000000
    Objeto                                1.000000
    Fundamento Legal                      1.000000
    Modalidade Compra                     1.000000
    Situação Contrato                     1.000000
    Código Órgão Superior                 1.000000
    Nome Órgão Superior                   1.000000
    Código Órgão                          1.000000
    Nome Órgão                            1.000000
    Código UG                             1.000000
    Nome UG                               1.000000
    Data Assinatura Contrato              1.000000
    Data Publicação DOU                   1.000000
    Data Início Vigência                  1.000000
    Data Fim Vigência                     1.000000
    Código Contratado                     0.958499
    Nome Contratado                       0.873387
    Valor Inicial Compra                  1.427405
    Valor Final Compra                    1.430633
    Número Licitação                      1.000000
    Código UG Licitação                   1.000000
    Nome UG Licitação                     1.000000
    Código Modalidade Compra Licitação    1.000000
    Modalidade Compra Licitação           1.000000

aqui vemos em porcentagem: 

1 = 100% 

0 = 0% 

Se for mais que um, significa que o consumo de memório atual em porcentagem é maior que
o consumo anterior.

Se igual a 1, não mudou nada

Se menor que 1, significa que o consumo de memória dos dados estão menor que anterior
'''