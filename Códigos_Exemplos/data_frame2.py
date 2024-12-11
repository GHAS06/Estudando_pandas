import pandas as pd 

'''
    LEIA A ANOTAÇÃO Pandas.txt e A_importância_do_type().txt
'''

# Criando Dataframe apartir de Series com listas e dicionários

s1 = pd.Series([10,20,39], name = 'c1')
s2 = pd.Series([30,40,50], name = 'c2')

'''
                            IMPORTANTE
df = pd.DataFrame([s1,s2])
print(df)

dessa forma com lista o pandas entende que cada serie é uma linha, não colunas, 
devemos tomar cuidado com isso.

SAIDA:

     0   1   2
c1  10  20  39
c2  30  40  50

# a mesma coisa acima só que usando os parâmetros

lista_coluna = [s1,s2]
df = pd.DataFrame(data = lista_coluna )
print(df)  

'''

'''

Para retornar a series como colunas, precisamos transfomá-los em dicionários
dicionários -> chave:valor
                        chave:valor|chave:valor
df = pd.DataFrame({'coluna1':s1, 'coluna2':s2})
print(df)

SAIDA:
   coluna1  coluna2
0       10       30
1       20       40
2       39       50

# a mesma coisa acima só que usando os parâmetros
lista_dicionário = {s1.name:s1, s2.name:s2}
df = pd.DataFrame(data = lista_coluna )
print(df)  

Aqui é um pouco diferente, porque eu puxei o nome(name) direto da serie para ser
a chave do meu dicionário

SAIDA:
   c1  c2
0  10  30
1  20  40
2  39  50
'''  

#Criando um DataFrame com colunas diferentes apartir de uma serie
#(Quantidade de linhas tipo)

s3 = pd.Series([10,20,40], name = 'c1')
s4 = pd.Series([30,40,50,60], name = 'c2')


'''
lista_dicionário = {s3.name:s3, s4.name:s4}
df = pd.DataFrame(data = lista_coluna )
print(df)

Veja! com colunas diferentes, seja tamanho, tipo ou quantidade de linhas a saida será
importante entender

SAIDA:
    c1  c2
0  10.0  30
1  20.0  40
2  40.0  50
3   NaN  60

o NaN (not a namber ) é uma espécie de NULL (não existe, não tem o número) 
'''
# exibindo informações do dataframe
'''
lista_dicionário = {s3.name:s3, s4.name:s4}
df = pd.DataFrame(data = lista_dicionário )

print(df.columns) # mostra as colunas do DataFrame e seu dtype
print(df.index) # mostra os indicies do DataFrame
'''

# Lista mutáveis e imutáveis

l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]

lista_dicionário = {'c1':l1,'c2':l2}

df_dic = pd.DataFrame(data=lista_dicionário)
print(df_dic)

'''
O valor dos dados que são listas em dicionários do df_dic pode ser alterado
diretamente nas listas, mas como o Pandas faz uma cópia dos dados ao criar o 
DataFrame, essas alterações nas listas não afetam o DataFrame. Ou seja, 
para esse DataFrame, as listas são mutáveis, mas as alterações nas listas 
não se refletem automaticamente no DataFrame.

SAIDA:
    c1  c2
0   1  10
1   2  20
2   3  30
3   4  40
4   5  50

Para mudar o valor dos dados neste DataFrame, vai ser necessário mudar o dado na
lista, exemplo -> l1 = [100,2,3,4,5]

SAIDA:
    c1  c2
0  100  10
1    2  20
2    3  30
3    4  40
4    5  50
'''

l1[0] = 100 # mudando o dado diretemente na lista com usando o indicie

x = pd.DataFrame(data=lista_dicionário)
print(f'\n{x}') 

'''
O DataFrame x foi criado a partir do dicionário lista_dicionário, que contém listas 
mutáveis como valores. Quando o valor de l1[0] foi alterado diretamente para 100, 
a modificação afetou o DataFrame x. Isso ocorreu porque, embora o Pandas normalmente 
faça uma cópia dos dados ao criar o DataFrame, ele ainda compartilha referências para
os dados originais se os dados não forem copiados explicitamente. Ou seja, quando as
listas mutáveis são passadas, qualquer alteração posterior nas listas de origem 
reflete nos dados do DataFrame.

No caso, o valor 100 apareceu na primeira linha da coluna c1 no DataFrame x, 
mostrando que a modificação na lista l1 foi refletida no DataFrame.

**Observação**: Para evitar esse tipo de comportamento, pode-se garantir que as listas 
sejam copiadas explicitamente (com o método .copy()) ao criar o DataFrame, assim as 
alterações nas listas originais não afetarão o DataFrame.

'''