import pandas as pd
import numpy as np

# descomente o que for necessário
# Esse quarto código o objetivo é mostrar filtros que podemos fazer com series

# criado series

a = pd.Series(np.random.rand(5))
b = pd.Series(np.random.rand(5))
#print(a)
#print(b)

# filtro com operadores de comparação
 
filtro_a = a[a >= 0.3]
filtro_b = b[b >= 0.5]

print(f'filtro_a:\n{filtro_a}\n')
print(f'filtro_b:\n{filtro_b}\n')

# filtro com operadores de compração entre as series

filtro_a_b = a[a > b]
print(f'Filtro_a_b:\n{filtro_a_b}\naqui retorna valores em que a é maior que os valores de b')

# Tem como fazer um vetor_lógico com valores booleanos para realizar filtros

# Índice booleano       #somente linhas
indices_booleanos = [True, False, True, False, True] 

# Aplicando o filtro
resultado = b[indices_booleanos]
print(f'\nAqui realizei um filtro com vetor_lógico para a serie_b:\n{resultado}')