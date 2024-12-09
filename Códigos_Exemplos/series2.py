import pandas as pd

# Descomente o que for necessário

Series = pd.Series({'a':10, 'b':2, 'c':40}, name= 'Valores')
#print(Series[['a','b']])

'''
descobrindo que tipo de dados é uma serie

print(type(Series))

saida -> <class 'pandas.core.series.Series'>

vimos que uma serie de fato é uma serie mas se modificarmos um pouco

print(type(Series[0]))

saida -> <class 'numpy.int64'>

descobrimos que ele retorna como um array do numpy, outra forma de fazer isso
é assim:

print(type(Series.array[1]))

saida -> <class 'numpy.int64'>

Retornando a serie como um array

print(Series.array)

SAIDA:

<NumpyExtensionArray>
[np.int64(10), np.int64(2), np.int64(40)]
Length: 3, dtype: int64


Retornando a serie como um array do numpy

print(Series.to_numpy())

saida -> [10  2 40]

'''

