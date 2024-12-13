import pandas as pd
from datetime import date 
# Essa código visa mostrar como funciona a função .raneme()

'''
    LEIA A ANOTAÇÃO: Renomeando_Colunas1.txt
'''
# lista de datas
lita_datas = [date(2024,12,12),date(2024,12,14),date(2024,12,10)]
# Criando um dicionário
dados = { 'Status':['Pago','Devendo','Pago'], 'Preço':[800,900,1000], 'Datas': lita_datas }
# Criando um DataFrame através de um diconário
alugueis = pd.DataFrame(dados)
print(alugueis.info()) # mostrando o tipo de dado de cada coluna

# CRIAR DICIONÁRIO PARA USAR NA FUNÇÃO .raname()
# Basicamente a chave é a coluna quereo renomear e o valor é o nome novo da coluna.

colunas = {'Status':'Situação','Preço':'Valor'}

# se usar o objeto dicionário, basta passar o objeto como parâmetro
print(alugueis.rename(colunas))
# podemos ter o mesmo resultado acima usando o parâmetro
print(f'\nColunas Modificadas:\n\n{alugueis.rename(columns=colunas)}')

# FORMA 2, RENOMEAR VÁRIAS COLUNAS DE UMA VEZ

print(alugueis.columns) # saida -> Index(['Status', 'Preço', 'Datas'], dtype='object')
print(type(alugueis.columns)) # saida -> <class 'pandas.core.indexes.base.Index'>

'''
 veja que retonarmos um atributo objeto do tipo index do dataframe 
 ao utilizar.columns
'''
# vamos transformar esse atributo em lista veja!

print(alugueis.columns.to_list()) # saida -> ['Status', 'Preço', 'Datas'] 
print(type(alugueis.columns.to_list())) # saida -> <class 'list'>

'''
    Veja, transformamos um objeto do pandas do tipo index para uma lista apartir
    desta informação, iremos realizar um bem bolado para renomear várias colunas
    de uma vez
'''

colunas_novas = ['Condição','Valia','Datas_Vencimento']

colunas = dict(zip(alugueis.columns.to_list(), colunas_novas))

print(alugueis.rename(columns=colunas))