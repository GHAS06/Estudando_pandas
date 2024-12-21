# Esse código visa desbravar o método sys.path da biblioteca sys 

import sys 
import os

'''
    LEIA A ANOTAÇÃO: sys.txt
    LEIA A ANOTAÇÃO: sys_2.txt
    LEIA A ANOTAÇÃO: OS.txt
    VEJA O Código Exemplo: Trabalhando_com_sys2.py
'''

# Vamos usar essa parte do código Adicionando_Colunas_em_DataFremas1.py
'''
    Lembre-se, sys.path retorna uma lista de strings que representa os diretórios onde o 
    Python busca por módulos.
'''

# Adiciona o diretório pai do script atual ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mostra caminhos intermediários para entendimento
print("Caminho relativo ao script atual:", os.path.join(os.path.dirname(__file__), '..'))
print("Caminho absoluto:", os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mostra os efeitos no sys.path
for x,path in enumerate(sys.path):
    #print(f'\nEssa é a lista de diretórios em sys.path: ')
    print(f"{x}:{path}")

'''
    SAIDA:
        ['c:\\Estudando_pandas'] 
    Veja, o caminho Estudando_pandas será adicionado no final da lista
'''

import pandas as pd
from funcoes_curso.leitura_arquivo import leitura_arquivos_csv, leitura_arquivos_excel

objeto = leitura_arquivos_csv('Arquivos_csv_estudos', '202401_Compras.csv')

# Verificando se o objeto que é a nossa função existe e não está vazio
if objeto is not None and not objeto.empty:
    print("Função executada com sucesso\n")
    print(objeto.head()['Número do Contrato'])  # Retornando as 5 primeiras linhas da coluna

# Link para aprender mais sobre listas em Python:
# https://docs.python.org/pt-br/3/tutorial/datastructures.html

'''
    Explicação sobre o que isso faz:

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    Resumidamente, estamos adicionando o caminho do diretório pai do script atual 
    à lista sys.path. Essa lista contém os diretórios onde o interpretador Python 
    busca módulos para importação durante a execução. Isso é útil quando precisamos 
    importar módulos que estão fora dos diretórios padrão acessíveis pelo Python.
'''

'''
Por que funciona?

Aqui está um exemplo mais detalhado:

O Python verifica cada diretório listado em sys.path até encontrar a pasta funcoes_curso
contendo o módulo leitura_arquivo.py.

Adicionando c:\\Estudando_pandas a sys.path:

Quando você adiciona o caminho c:\\Estudando_pandas ao sys.path, o Python passa a procurar
dentro dele. Ou seja, a estrutura de diretórios que você criou dentro de Estudando_pandas
fica acessível para importação. No caso, se a pasta funcoes_curso está dentro de 
c:\\Estudando_pandas, o Python encontra a pasta porque esse caminho já está no sys.path.

Estrutura de diretórios:

c:\Estudando_pandas
│
├── funcoes_curso
│   ├── __init__.py  # Indica que "funcoes_curso" é um pacote (opcional no Python 3.x)
│   ├── leitura_arquivo.py
│   
└── script_principal.py
'''
