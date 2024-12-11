import pandas as pd
import os

# Essa parte visa explicar a manipulação de colunas bem como a alteção dos seus dados

# Adquirindo dados de um arquivo csv usando a biblioteca os para construir caminhos

caminho_atual = os.getcwd()
#print(caminho_atual) # usamos para adquirie o diretório atual

caminho_arquivo = os.path.join(caminho_atual,'Arquivos_csv_estudos','ItemsCompra.csv')
#print(caminho_arquiv) # usamos para combinar caminhos de forma segura


