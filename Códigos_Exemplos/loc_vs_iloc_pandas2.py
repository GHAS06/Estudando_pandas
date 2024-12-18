import pandas as pd

'''
    LEIA A ANOTAÇÃO: ILOC_VS_LOC_2.txt
'''

# Craindo DataFrame
dados = dados = {
            
    "Produtos":['Flores','Carne','Churros'],
    "Quantidade":[10,20,30],
    "Preço":[5.0,10.0,15.0]
}

datas = pd.date_range('16/12/2024', periods = 3) 
     
df = pd.DataFrame(dados, index = datas )
print(df) 

# Selecionando usando loc

# retornando ele como uma Series   
print(df.loc[datas[0],['Produtos','Preço']])
print(type(df.loc[datas[0],['Produtos','Preço']]))

'''
SAIDA: 
     
    Produtos    Flores
    Preço          5.0
    Name: 2024-12-16 00:00:00, dtype: object
    <class 'pandas.core.series.Series'>
    
    # Retornou como series porque acessamos diretamente uma linha com seu index

'''

# retornando ele como um Dataframe
print(df.loc[datas[[0]],['Produtos','Preço']])
print(type(df.loc[datas[[0]],['Produtos','Preço']]))

'''

# retornou como DataFram porque acessamos multiplas linha com uma lista

    SAIDA:
              Produtos  Preço
    2024-12-16   Flores    5.0
    <class 'pandas.core.frame.DataFrame'>
'''
    # Selecionado multiplas linhas com o loc

print(df.loc[datas[0:2],['Produtos','Preço']])
print(type(df.loc[datas[0:2],['Produtos','Preço']]))
print(type(df.index[0:2]))

'''
    Veja! Usei um intervalo entre o index 0 de datas até o index 2
    e o  pandas entendeu de maneira diferente, agora ele não retornou como apenas uma 
    series, ele retornou como um DataFrame. Por que? Porque agora, não estamos apenas
    puxando uma linha do nosso DataFrame, estamos puxando um intervalo com o nosso slice
    [intervalo], basicamente, o slice gera uma coleção de índices (DatetimeIndex)

                Produtos  Preço
     2024-12-16   Flores    5.0
     2024-12-17    Carne   10.0
     <class 'pandas.core.frame.DataFrame'>
     <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
     
     # isso acima, sem selecionar uma linha especificamente é o mesmo que fazer:

     print(type(df.loc[datas[[0]],['Produtos','Preço']]))
'''

# Usando Caracteres especiais para selecionar multiplas linhas e colunas:

#  Podemos usar o : para representar todos as nossa linhas ou colunas

print(df.loc[:,['Produtos','Preço']])
# retorna todas as linhas e essas duas colunas

print(df.loc[:,:])
# retonra todas as linhas e colunas do DataFrame

# Selecionando por rótulos
print(df.loc[datas[0:2],"Produtos":"Preço"])
# outra forma de retorna todas as linhas e colunas

# Selecionando com .iloc[] utilizando Atributos do DataFrame
print()
print()
print(df.iloc[0:2].Preço)
print(type(df.iloc[0:2].Preço))
print()
print()
print(df.iloc[0:2][['Produtos', 'Preço']])
print(type(df.iloc[0:2][['Produtos', 'Preço']]))