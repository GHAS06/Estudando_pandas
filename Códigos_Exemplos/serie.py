import pandas as pd 

# Criando uma Serie para treinar diferença entre Serie e Data Frame
# Descomente o que for necessário

'''

Quando o assunto são dados em series ou dataframes, o pandas irá trabalhar da forma
mais genérica possível, se não especificarmos seu tipo de dados.

Veja! na segunda serie, tem um dado do tipo flaot64 e o restante é int64
então ele converteu os dados de int64 para float64

na terceire serie, temos dados int64, float64 e um dado object, como o pandas 
não sabe muito bem distinguir o que tá acontecendo, ele converteu tudo para 
object

'''

'''
Uma serie de dtype = int64

Serie = pd.Series([10,20,30,40])
print(Serie)
'''

'''
Uma serie de dtype = float64

Serie = pd.Series([10,20,30,40,6.5])
print(Serie)

'''


'''
Uma serie de dtype = object

Serie = pd.Series([10,20,30,40,6.5, '90'])
print(Serie)

'''

'''
Serie de dtype = float64 porque convertemosa lista de int para float na serie 

list_num = [1,2,3,4]
Serie = pd.Series(data = list_num, dtype = float)
print(Serie)

'''

'''
Aqui só coloquei letras alfabeticas como indicies no parâmetro index

list_num = [1,2,3,4]
Serie = pd.Series(data = list_num, dtype = float, index = ['a','b','c','d'])
print(Serie)

'''

'''
Também é possível fazer uma serie com dionário, mas o indicie é a chave 
enquanto o valor é o dado propriamente dito.

Series = pd.Series({'a':10, 'b':2, 'c':40})
print(Series)

'''

'''
Fazendo Slice com os indicies da series para poder acessar determinados dados

list_num = [1,2,3,4]
Serie = pd.Series(data = list_num, dtype = float, name = 'Valores')

print(Serie[0:2])

SAIDA:

0    1.0
1    2.0
Name: Valores, dtype: float64

colocamos um nome nessa serie, é uma boa prática fazer isso para identificarmos 
mais facilmente as informações da nossa serie ou dataframe

'''

'''

Acessando dados específicos da series com uma lista de indicie

Series = pd.Series({'a':10, 'b':2, 'c':40})
print(Series[['a','b']])

'''