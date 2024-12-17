import pandas as pd
import numpy as np

# Esse código visa mostrar como funciona a indexação para a estrutura dados DataFrame.

'''
    RECOMENDO FORTEMENTE 

    LEIA A ANOTAÇÃO: Indexação_e_atributos.txt
    LEIA A ANOTAÇÃO: A_importância_do_type().txt
'''

# Indexação usando (números, letras, objetos, funções, atributos e entre outros)

 # Criando um DataFrame: 
#df = pd.DataFrame(np.random.rand(3,3), index = range(5,8), columns = [*"ABC"])
df = pd.DataFrame(np.random.rand(3,3), columns = [*"ABC"])
#df = pd.DataFrame(np.random.rand(3,3))  # Index e Columns padrão
print(df)

print(type(df.index)) # saida -> <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
# os dois modos retornaram o mesmo tipo de dados
print(type(df.columns)) # saida -> <class 'str'> modo modificado
#print(type(df.columns)) # saida -> <class 'pandas.core.indexes.range.RangeIndex'> modo padrão

'''
    SAIDA:
                  A         B         C
        5  0.123456  0.789123  0.456789
        6  0.987654  0.345678  0.123456
        7  0.654321  0.234567  0.987654

Veja! Indexamos por um range de índice baseado em um intervalo sequencial de números 
inteiros. Por Padrão o Pandas já realiza esse tipo de indexação.

Já as colunas, por mais que tenhamos renomeado ela, na verdade, simplemente atribuimos 
um valor que sobrescreve o index das colunas.

Quando fizemos um print(type(df.columns)) no df com as colunas modificadas ele retornou
como <class 'pandas.core.indexes.base.Index'>

A classe <class 'pandas.core.indexes.base.Index'>

representa o tipo do objeto Index no pandas, que é utilizado para armazenar os índices
de um DataFrame ou Series.

Esse tipo é retornado quando você acessa a propriedade index de um DataFrame ou Series que
não tem um índice de tipo específico, como um RangeIndex ou DatetimeIndex. Ele serve como
uma base para os índices de tipos mais especializados, como RangeIndex, DatetimeIndex, etc.

Se você estiver criando um DataFrame com colunas ou linhas indexadas com dados
personalizados, o pandas criará um Index genérico para essas informações.

'''

# Indexação de linhas com datas

datas = pd.date_range('16/12/2024', periods = 3) # função que cria uma sequência de datas
# Excelente para análises temporais

print()
print(type(datas)) # saida -> <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
print()

df_com_datas = pd.DataFrame(np.random.rand(3,3), index = datas, columns = [*"ABC"])
print(df_com_datas)

'''
    SAIDA:
                   A         B         C
2024-12-16  0.110086  0.646747  0.668850
2024-12-17  0.641869  0.509620  0.012475
2024-12-18  0.823998  0.323555  0.006006

VEJA! Resumidamente Aqui usamos datas para indexar este DataFrame
'''

# Indexando como atributo

df.index = [1,2,3]

# O mesmo para as Colunas

df.columns = [*'CDF']

print(df)