import pandas as pd

# Esse código visa mostrar como funciona asa funções loc e iloc
'''
    LEIA A ANOTAÇÃO: LOV_VS_ILOC.TXT
'''

# ler arquivo csv
df = pd.read_csv(r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_Compras.csv",encoding='latin1',sep = ";", header=0, nrows=10, usecols=["Número do Contrato","Objeto","Fundamento Legal"])

# Usando o loc para selecionar através de linhas(seus indicies) e colunas(seus nomes)
#print(df.loc[0:3, "Número do Contrato"])

#podemos especificar as linhas, colocando dentro de uma lista
#print(df.loc[[1,2,5,6]])

# Usando o iloc para selecionar um intervalo de linhas através do seu indicies
#print(df.iloc[0:6])

# o indicie serve para colunas também
#print(df.iloc[0:6, 0:2])

'''
Observação o iloc não exibe a posição que estamos, sempre uma posição anterior
Quando tratamos de situções True or False nno iloc, isso pode impactar na filtragem

'''
