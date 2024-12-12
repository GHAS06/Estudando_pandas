import pandas as pd
import os
from pandasgui import show

# Essa parte visa explicar a manipulação de colunas bem como a alteção dos seus dados
# também visa a utilização do pandasgui para vizualizarmos os dataframes tratados

'''
    LEIA A ANOTAÇÃO: PANDAS.txt
    LEIA A ANOTAÇÃO: Manipulação_Colunas.txt
    LEIA A ANOTAÇÃO: Abrindo_arquivos_com_libs.txt
    LEIA A ANOTAÇÃO: A_importância_do_type().txt
    LEIA A ANOTAÇÃO: Tratamento_da_dados1.txt    
'''


# Adquirindo dados de um arquivo csv usando a biblioteca os para construir caminhos

caminho_atual = os.getcwd()
#print(caminho_atual) # usamos para adquirie o diretório atual

caminho_arquivo = os.path.join(caminho_atual,'Arquivos_csv_estudos','202401_itemCompra.csv')
print(caminho_arquivo) # usamos para combinar caminhos de forma segura

# um arquivo_csv é um DataFrame
df = pd.read_csv(caminho_arquivo, encoding='latin1', sep = ';')
print(type(df)) # saida -> <class 'pandas.core.frame.DataFrame'>

#print(df.head()) # retorna as 5 primeiras linhas
#print(df.info()) # retorna informações das colunas e seus tipos de dados

# variável que armazena uma lista com os nomes das colunas
lista_colunas_csv = [ 
    'Código Órgão',                         
    'Nome Órgão',                          
   'Código UG',                           
   'Nome UG',                             
   'Número Contrato',                      
   'Código Item Compra',                  
   'Descrição Item Compra',               
   'Descrição Complementar Item Compra',  
   'Quantidade Item',                      
   'Valor Item'         ]

# uma coluna do DataFrame é uma series
#series = df[lista_colunas_csv[9]]
#print(series) # dtype -> Objetc(String) vamos usar essa coluna para manipular
#print(type(series)) # saida -> <class 'pandas.core.series.Series'>

# tentando mudar o separador de milar ',' por ponto '.'
#series.replace(',','.') # replace serve para substituir 
#print(series) # a saida não tivemos sucesso na substituição

# fazendo essa substituição forçadamente com string 
#series.str.replace(',','.')
#print(series)  # também não tivemos sucesso na substituição

# Funções apply() excelentes para trabalhar com Series

# convertendo objetc para float
#series_tratada = series.apply(lambda x: float(x.replace(',','.')))
#print(series_tratada.head())

'''
    Agora obtemos sucesso na hora de realizar o tratamento dos dados, e convertemos
    a coluna de objetc(string) para float

SAIDA:
    0           8044,26
    1        2100000,00
            ...
    11988         88,89

Name: Valor Item, Length: 11989, dtype: object

<class 'pandas.core.series.Series'>

    0           8044.26
    1        2100000.00
    2            530.00
                ...

    11988         88.89
    Name: Valor Item, Length: 11989, dtype: float64

poderia encadear com outro .replace() na lambda, poderia encadear um outro apply()
mas não vou fazer, porém é possível fazer isso, mas não é uma boa prática.

'''

# função .applymap() exclusiva realizar manipulação e tratamento de dados em Dataframe

# selecionando todas as linhas de colunas específicas para o DataFrame_1
#DataFrame_1 = df.loc[:,[lista_colunas_csv[0],lista_colunas_csv[8],lista_colunas_csv[9]]]
#print(DataFrame_1.info())
#print(DataFrame_1.head())

# utilizando o applymap() para realizar o tratamento de dados de uma coluna

#DataFrame_1_tratado = DataFrame_1[[lista_colunas_csv[9]]].applymap(lambda y: float(y.replace(',','.')))
#print(DataFrame_1_tratado.head())
#print(type(DataFrame_1_tratado))

'''
SAIDA:
   Valor Item
0     8044.26
1  2100000.00
2      530.00
3   400827.75
4   110051.67

<class 'pandas.core.frame.DataFrame'>

Por mais que senha modificado só uma coluna, continuou sendo um DataFrame

'''

#utilizando o applymap() para realizar o tratamento de dados em multiplas colunas
#DataFrame_1_tratado = DataFrame_1.applymap(lambda z: float(z.replace(',', '.')) if isinstance(z, str) else z) 
#print("\nDataFrame modificado:")
#print(DataFrame_1_tratado.head())

'''
A função isinstance() no Python é usada para verificar se um objeto é de um 
determinado tipo. Ela retorna True se o objeto for do tipo especificado e False 
caso contrário.

SINTAXE: isinstance(obj, classinfo)

obj -> O objeto a ser testado.
classinfo -> A classe ou tipo a ser verificado.

CONTEXTO DISSO NO CÓDIGO:
    
    estamos usando isinstance(z, str) para garantir que replace() seja chamado 
    apenas em valores que são strings, evitando assim o erro AttributeError: 'int' 
    object has no attribute 'replace'.

SAIDA:

    DataFrame modificado:
   Código Órgão  Quantidade Item  Valor Item
0         20301                1     8044.26
1         26290                2  2100000.00
2         26290             1000      530.00
3         26290                1   400827.75
4         26245               12   110051.67
'''

# Adcionando colunas Total_compra com base nas informações
#DataFrame_1_tratado['Total_compra'] = DataFrame_1_tratado[lista_colunas_csv[8]] * DataFrame_1_tratado[lista_colunas_csv[9]]

# Vizualização rápida com pandas no terminal
#print(DataFrame_1_tratado.head())

# Usando PandasGui para uma Vizualização mais Robusta e completa dos dados
#show(DataFrame_1_tratado)

# com base na vizualização que tivemos no show(DataFrame_1_tratado)
# Fizemos um filtro para descobrir o Orgão que comprou intens

#filtrar_orgão = df[(df['Código Órgão'] == 36000)]
#print(f'\nFiltrando Dados do órgão que mais comprou intens:\n')
#print(filtrar_orgão.loc[:,[lista_colunas_csv[1],lista_colunas_csv[2],lista_colunas_csv[6],lista_colunas_csv[7]]].head())
#print(filtrar_orgão.head())

# vizualizar todas as tabelas
#show(filtrar_orgão.loc[:,[lista_colunas_csv[1],lista_colunas_csv[2],lista_colunas_csv[6],lista_colunas_csv[7]]])

# realizando um bem bolado da analise de dados kkk

# Seleciono todas as linhas e colunas do DataFrame
DataFrame_1 = df.loc[:,:]
# Realizo o tratamento e conversão dos valores da coluna Valor Item
Valor_Item_Tratado = DataFrame_1[[lista_colunas_csv[9]]].applymap(lambda y: float(y.replace(',','.')))
#Armazeno o objeto DataFrame_1 em uma variável DataFrame_1_tratado
DataFrame_1_tratado = DataFrame_1
# Faço o insert do Valor_Item_Tratado no DataFrame
DataFrame_1_tratado.insert(9, 'Valor Item Tratado', Valor_Item_Tratado)   

# Adicionando a coluna Total_Compra como floar
DataFrame_1_tratado['Total_Compra'] = (
    DataFrame_1_tratado['Quantidade Item'] * DataFrame_1_tratado['Valor Item Tratado']
).astype(float)  # Realizamos um agrupamento para o cálculo e Converte explicitamente para float
#Removo a coluna Valor Item que é tipo Object, não é o Tratado
del DataFrame_1_tratado['Valor Item']
# Exibo as informações do DatraFrame
print(DataFrame_1_tratado.info())   

# Vizualizar os dados
show(DataFrame_1_tratado)
