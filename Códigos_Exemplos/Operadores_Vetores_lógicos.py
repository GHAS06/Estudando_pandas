import pandas as pd

# Esse código visa mostrar a seleção e filtragem com vetores e operadores lógicos

'''
    LEIA A ANOTAÇÃO: Usando_e_entendendo_Vetores_Lógicos.txt
    LEIA A ANOTAÇÃO: Selecionando_colunas.txt
    LEIA A ANOTAÇÃO: Manipulando_Colunas_DataFrame.txt
'''
dados = {'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [25, 30, 35]} 
df = pd.DataFrame(dados, index=['a', 'b', 'c'])

#usando loc com vetores lógicos, o primeiro represenda as linhas
#o segundo vetor representa as colunas
print(df.loc[[True,True,False],[True,False]])

#Entendendo como pandas faz operações lógicas no DataFrame

#print(df.Nome == "Alice")

'''
A saida de informação deste print foi:

a     True
b    False
c    False


Logo, vemos que, a linha de indicie 'a' tem o nome Alice.
Enquanto os outros não tem.

Basicamente, puxamos uma única coluna do nosso DataFrame e fizemos uma comparação
para os atributos daquela coluna, se os atributos estivesse o nome Alice, no retorno
do vetor lógico, ele teria valor boolean True
'''

# Apartir desta informação podemos fazer um Filtro com os Vetores Lógicos, Veja! 

#print(df[df.Nome == "Alice"])

'''
Veja que interessante, através do vetor lógicos conseguimos fazer um filtro para 
retornar valores do nosso DataFrame que contenha o nome Alice 

    Nome  Idade
a  Alice     25

'''
'''
    Com essa informação de filtragem, podemos fazer um filtro usando os operadores 
    lógicos and(&) ou or(ou)
'''
#print(df[(df.Nome == "Alice") & (df.Idade == 25)])
'''
em parenteses,dentro de colchete, neste caso, os dois valores devem ter valor lógico
verdadeiro para retornar no filtro.
'''

#Realizando a filtragem com ou |

#print(df[(df.Nome == "Alice") & ((df.Idade == 25) | (df.Idade == 30))])

'''
    Lembre-se: os parenteses nesse modo de filtrarm irá definir como funciona 
    as operações, limitador da filtragem com operadores lógicos e vetores lógicos
'''