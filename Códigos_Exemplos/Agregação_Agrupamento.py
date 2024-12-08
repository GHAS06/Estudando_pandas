import pandas as pd

'''
O objetivo aqui é usar as funções de agregamento junto com alguma função de
agrupamento groupby() 
Também vamos usar filtros com vetores_lógicos e operadores com iloc ou loc
'''
caminho_arquivo_csv = r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_ItemCompra.csv"
df  = pd.read_csv(caminho_arquivo_csv, encoding= 'Latin1', sep = ';')

# Usando o df.info para tirar informções das colunas
#df.info()
# exibindo as 5 primeiras linhas
#print(df.head())
colunas = [ 
    
    'Código Órgão',                      
    'Nome Órgão',                          
    'Código UG',                           
    'Nome UG',                             
    'Número Contrato',                    
    'Código Item Compra',                 
    'Descrição Item Compra',              
    'Descrição Complementar Item Compra',  
    'Quantidade Item',                     
    'Valor Item'   
]

# Contruindo o filtro como vetores lógicos e ordenando da maior quantidade para a menor

filtro = df[(df['Código Órgão'] == 26290) & (df['Quantidade Item'] >= 2)].sort_values(['Quantidade Item'], ascending=False)

# Selecionando colunas específicas com iloc
resultado = filtro.iloc[:, [0,1,2,8,9]] 
print(resultado)

# Usando a lista 'colunas' para selecionar as colunas pelos nomes (como uma sublista)7
# usando o loc
#resultado = filtro.loc[:, [colunas[0], colunas[1]]]
#print(resultado)

'''
Por que o : sozinho?
O Pandas precisa saber se você está se referindo às linhas ou colunas do DataFrame.

Antes da vírgula (:): Significa todas as linhas.
Depois da vírgula (:): Significa todas as colunas.  
Se você usar apenas o : em uma das posições, o Pandas entende que deseja "tudo" naquela dimensão.
'''

# USANDO O GROUPBY para agregar e agrupar

#resultado_agrupado = resultado[['Código Órgão','Quantidade Item']].groupby(['Código Órgão']).sum()
#print(resultado_agrupado)

#df_agrupado = df[['Código Órgão','Quantidade Item']].groupby('Código Órgão').sum()
#print(df_agrupado)

'''
Este código está agrupando os dados pelo 'Código Órgão' e somando os valores da coluna
'Quantidade Item' para cada grupo. O resultado final é uma tabela onde cada 
'Código Órgão' tem a soma das 'Quantidade Item' associadas a ele.
'''