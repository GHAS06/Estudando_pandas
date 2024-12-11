import pandas as pd

# Descomentar o que for necessário 

'''
 Essa parte do código visa mostrar como funciona o type() para identificação
 dos tipos de dados invisíveis ou implícitos.

    LEIA A ANOTAÇÃO A_importância_do_type()
'''

a = 10
b = '10'
c = 10.0
d = tuple('Cachorro')
e = ['10']
f = {30}
g = {0:10}

#print(type(a))
#print(type(b))
#print(type(c))
#print(type(d))
#print(type(e))
#print(type(f))
#print(type(g))

#Serie = pd.Series([a,b,c,d,e,f], name = 'Coluna1')
#print(Serie)
#print(type(Serie))


#print(type(Serie[0]))  # Saída: <class 'int'>
#print(type(Serie[1]))  # Saída: <class 'str'>
#print(type(Serie[2]))  # Saída: <class 'float'>

s1 = pd.Series([1, 2, 3, 4, 5], name='c1')
s2 = pd.Series([10, 20, 30, 40, 50], name='c2')
Series = pd.Series({'a':10, 'b':2, 'c':40}, name= 'Valores')
    
print(type(Series[0])) # saida -> <class 'numpy.int64'>

''' 
descobrimos que ele retorna como um array do numpy, quando fazemos o slice de
 um indicie da series, outra forma de fazer isso é assim:
'''

print(type(Series.array[1])) #saida -> <class 'numpy.int64'>



# Criando um DataFrame

df = pd.DataFrame({s1.name: s1, s2.name: s2})
    
print(type(df['c1'])) #saida -> <class 'pandas.core.series.Series'>

print(type(df[['c1','c2']])) #saida -> <class 'pandas.core.frame.DataFrame'>

print(type(df['c1'][0])) # saída -> <class 'numpy.int64'>