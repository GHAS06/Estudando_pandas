import pandas as pd

df = pd.read_csv(r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_Compras.csv",encoding='latin1',sep = ";", header=0, nrows=10)

# listando informações do arquivo csv com tabelas e seu tipos de dados
#print(df.info())

# Ordenando por Código UG usando o by
'''
dados_ordenados = df.sort_values(by='Código UG')
print(dados_ordenados)
'''
# ordenando sem o by
'''
dados_ordenados = df.sort_values(['Código UG'])
print(dados_ordenados, ascending = False)
'''

# Podemos colocar um parâmetro ascending = True (funciona como o ASC) e False
#(funciona como o DESC) do sql

'''
Quando ascending=True (que é o valor padrão), os dados são classificados em ordem
crescente.

Quando ascending=False, os dados são classificados em ordem decrescente.
'''