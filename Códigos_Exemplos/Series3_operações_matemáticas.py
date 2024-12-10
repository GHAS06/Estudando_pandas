import pandas as pd
import numpy as np

# descomente o que for necessário

'''
Podemos faze algumas operações matemáticas com series depois de entender como 
funciona o seu tipo de dados e estrutura nos códigos anteriores, vou usar vetores
do numpy como exemplo para esse terceiro código

Vamos realizar operações elementares entre duas séries e com valores escalares.

'''

# Craindo Series

a = pd.Series(np.random.randn(5))
b =  pd.Series(np.random.randn(5))

'''
não vai impactar tanto aqui porque os vetores possuem o mesmo tamanho
''' 
# Operações matemáticas entre as séries
print(f'Adição entre Series:\n{(a + b).round(2)}\n')
print(f'Subtração entre Series:\n{(a - b).round(2)}\n')
print(f'Multiplicação entre Series:\n{(a * b).round(2)}\n')
print(f'Divisão entre Series:\n{(a / b).round(2)}\n')
print(f'Módulo entre Series:\n{(a % b).round(2)}\n')
print(f'Potenciação entre Series:\n{(a ** b).round(2)}\n')


# vai funcionar para o restante das operações matemáticas entre as series

'''
    Agora muda quando estamos fazendo de maneira escalar.É Quando somamos uma série
    com um escalar(constante), o valor é somado a todos os elementos da série.
    o mesmo vai funcionar para todas as outras operações matémáticas de maneira 
    escalar
'''
# Operações matemáticas escalares
print(f'Adição escalar:\n{(a + 10).round(2)}\n')
print(f'Subtração escalar:\n{(a - 10).round(2)}\n')
print(f'Multiplicação escalar:\n{(a * 10).round(2)}\n')
print(f'Divisão escalar:\n{(a / 10).round(2)}\n')
print(f'Módulo escalar:\n{(a % 10).round(2)}\n')
print(f'Potenciação escalar:\n{(a ** 2).round(2)}\n')
# o 10 é o nosso escalar

# Operações com alinhamento e preenchimento de valores faltantes
'''
Para lidar com índices desiguais, você pode preencher valores faltantes antes de
realizar a operação, usando métodos como .add() com o parâmetro fill_value.
'''
c = pd.Series(np.random.randn(3), index=['x', 'y', 'z'])
d = pd.Series(np.random.randn(5), index=['a', 'b', 'x', 'y', 'z'])
print(f'Alinhamento entre Series:\n{c + d}\n')
print(f'Adição com preenchimento de valores faltantes:\n{c.add(d, fill_value=0)}\n')

# Operações acumulativas com Series
'''
Operações acumulativas em Pandas referem-se a cálculos que acumulam valores de uma 
Série ou DataFrame ao longo de suas linhas ou colunas. Em vez de operar apenas em 
pares de valores, elas computam um resultado acumulado progressivamente, mantendo
o histórico das operações realizadas até cada ponto da estrutura de dados.
'''
print(f'Série original:\n{a}\n')
print(f'Adição acumulativa (cumsum):\n{a.cumsum()}\n')
print(f'Multiplicação acumulativa (cumprod):\n{a.cumprod()}\n')
print(f'Máximo acumulativo (cummax):\n{a.cummax()}\n')
print(f'Mínimo acumulativo (cummin):\n{a.cummin()}\n')


