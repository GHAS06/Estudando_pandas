# importando libs
import sys
import os
import time
import requests 
import pandas as pd
from pandasgui import show

try:
    # realizando testes para saber qual diretório estou
    print(os.getcwd())

    # fazendo um caminho absoluto para o interpretador python ler
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # puxando o ultimo item da lista de módulos lida pelo interpretador
    print(sys.path[-1])

except Exception as e:
    print(f"Erro: {e}")
        
from funcoes_curso.leitura_arquivo import leitura_arquivos_excel

# Objetivo aqui é fazer uma análise exploratório, parte 1

# vamos usar as funções: .nunique(), .describe(include = 'all'), .info(), .dtypes()
# usar também o método type()