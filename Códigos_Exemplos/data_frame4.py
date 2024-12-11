import pandas as pd
import os

# Essa parte visa explicar a manipulação de colunas bem como a alteção dos seus dados
'''
    LEIA A ANOTAÇÃO: PANDAS.txt
    LEIA A ANOTAÇÃO: Manipulação_Colunas.txt
    LEIA A ANOTAÇÃO: Abrindo_arquivos_com_libs.txt
    LEIA A ANOTAÇÃO: A_importância_do_type().txt    
'''


# Adquirindo dados de um arquivo csv usando a biblioteca os para construir caminhos

caminho_atual = os.getcwd()
#print(caminho_atual) # usamos para adquirie o diretório atual

caminho_arquivo = os.path.join(caminho_atual,'Arquivos_csv_estudos','202401_itemCompra.csv')
#print(caminho_arquiv) # usamos para combinar caminhos de forma segura

df = pd.read_csv(caminho_arquivo, encoding='latin1', sep = ';')
print(type(df)) # saida -> <class 'pandas.core.frame.DataFrame'>

print(df.head())

# uma coluna do DataFrame é uma serie
series = df['Nome Órgão']
print(type(series)) # saida -> <class 'pandas.core.series.Series'>


