import os
import pandas as pd
from pathlib import Path

# Esse código visa mostrar formas de ler aquivos usando libs com pandas
'''
    VEJA O CÓDIGO: pd_read_arquivos.py.txt
    LEIA A ANOTAÇÃO: Abrindo_arquivos.txt
    LEIA A ANOTAÇÃO: Abrindo_Arquivos_lib.txt
    LEIA A ANOTAÇÃO:
    LEIA A ANOTAÇÃO:
    LEIA A ANOTAÇÃO:    
'''

'''
# Diretório base
diretorio_base = os.getcwd()
# o diretório atual é a pasta Estudando_pandas, com isso consigo contruir um caminnho 

# Construindo o caminho correto
caminho_arquivo = os.path.join(diretorio_base, 'Arquivos_csv_estudos', '202401_ItemCompra.csv')

# Verifique o caminho gerado
print("Caminho do arquivo:", caminho_arquivo)

# Tente carregar o arquivo
try:
    df = pd.read_csv(caminho_arquivo, encoding= "latin1", sep =';')
    print(df.head())

except FileNotFoundError as e:
    print(f"Erro: {e}")
'''

'''
# usando o pathlib para realizar a mesma coisa acima
diretório_atual = Path.cwd()

Construindo_caminho = Path.joinpath(diretório_atual, 'Arquivos_csv_estudos', '202401_ItemCompra.csv')

try:
    df = pd.read_csv(Construindo_caminho, encoding='latin1',sep=';')
    print(df)   
except Exception as e:
    print(f'Ocorreu um erro): {e}')
'''

# usando os dois, tanto o os e o pathlib

diretório_base = Path(os.getcwd())

caminho_construido = diretório_base.joinpath('Arquivos_csv_estudos', '202401_ItemCompra.csv')

#print(str(caminho_construido))

try:
    df = pd.read_csv(caminho_construido,encoding='latin1',sep=';')  
    print(df)
except Exception as e:
    print(f'Ocorreu um erro: {e}')