import pandas as pd

# Esse código visa explicar como funciona os filtros com pandas
'''
    LEIA A ANOTAÇÃO: LOC_VS_ILOC.txt
    LEIA A ANOTAÇÃO: Filter_Filtro_dados.txt
    LEIA A ANOTAÇÃO:Usando_e_entendendo_Vetores_Lógicos.txt
'''
df = pd.read_csv(r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_Compras.csv",encoding='latin1',sep = ";", header=0, nrows=10)

#print(df.info())

#filtrando através de colunas
'''
df_filtrado = df[['Nome Órgão','Código UG']]
print(df_filtrado)
'''
#filtando através de colunas com o parâmetro items
'''
df_filtrado = df.filter(items=['Nome Órgão','Código UG','Nome UG'])
print(df_filtrado)
'''

#filtrando usando o parâmetro like
'''
df_filtrado = df.filter(like = 'UG')
print(df_filtrado.head())
'''
#filtrando usando o parâmetro regex
'''
df_filtrado = df.filter(regex = '.UG.')
print(df_filtrado)
'''