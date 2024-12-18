import pandas as pd

dados = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Nome": [
        "Ana", "Bruno", "Carla", "Diego", "Eva", "Felipe", "Gabriela", "Heitor",
         "Iris", "João"],
    "Idade": [23, 35, 29, 40, 18, 25, 32, 45, 28, 50],
    "Salario": [3000, 5000, 4000, 8000, 2000, 3500, 4500, 9000, 3800, 10000],
    "Setor": ["RH", "TI", "TI", "RH", "Vendas", "Vendas", "TI", "RH", "RH", "TI"],
    "Ativo": [True, True, False, True, False, True, False, True, True, False],
    "Avaliação": [8.5, 9.2, 6.8, 7.9, 5.4, 7.2, 8.0, 9.0, 7.5, 6.0] 
}

# Criando o DataFrame
df = pd.DataFrame(dados)
print(type(df)) # vai retornar um DataFrame
# Retronando um vetor_lógico do tipo Series
print(df.Salario > 3000)
print(type(df.Salario > 3000))
'''
0    False
1     True
2     True
3     True
4    False
5     True
6     True
7     True
8     True
9     True
Name: Salario, dtype: bool
<class 'pandas.core.series.Series'>
'''
# Podemos obter o mesmo resultaado acima usando a função .loc[]
print()
print(df.loc[:,'Salario'] > 3000)
print()
# Filtragem usando vetores lógicos
print(df[df.loc[:,'Salario'] > 3000]) # puxar todas as linhas e coluans que respeitam essa condição
print()
print(type(df.loc[:,'Salario'] > 3000))
# Fazendo Filtragem usando vetores_lógicos e operadores lógicos

print(df[(df.loc[:,'Salario'] > 3000) & (df['Ativo'] == True)])
print(type((df.loc[:,'Salario'] > 3000) & (df['Ativo'] == True)))

# Verificando se os dados retornam de fato um DataFrame
#df_filtro = df[(df.loc[:,'Salario'] > 3000) & (df['Ativo'] == True)]
#print(type(df_filtro)) # Saida -> <class 'pandas.core.frame.DataFrame'>

# trabalhando com os outros operadores lógicos
print()
print(df[(df.loc[:,'Salario'] >= 3000) | (df['Ativo'] == True) & (df.loc[:,'Setor'] == 'RH')])
print()
# sinceramente não sei que bagaceira de filtro é essa. Mas retorna dados sem depender do RH
print()
print(df[(df.loc[:,'Salario'] > 3000) & (df['Ativo'] == True) & ~(df.loc[:,'Setor'] == 'RH')])
print()
# Retorna dados do DataFram em que os funcionários ativos recebem mais que 3000 sem ser do Setor do RH
print()
print(df[(df.loc[:,'Nome'] == 'Bruno') & (df['Ativo'] == True) & (df.loc[:,'Setor'] == 'TI')])
print()
# Aqui vai retornar o Bruno que Trabalha no Setor da T.I´
print()
print(df[(df.loc[:,'Nome'] == 'Bruno') & ((df['Ativo'] == True) | (df.loc[:,'Setor'] == 'TI'))])
print()
# cuidado com os parenteses, aqui vai retornar o bruno que trabalha na TI ou outros Brunos que Trabalham em outra áreas desde que esteja ativo