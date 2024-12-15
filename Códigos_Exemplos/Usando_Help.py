# Copiei do código Adcionando_Colunas_em_DatasFrame2.py

import sys
import os

# Adiciona o diretório base ao sys.path
# Estava dando erro aqui, copiei do chat, estude essa lib sys #copiei do código1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora os imports devem funcionar
import pandas as pd
import numpy as np
from datetime import time

# Com essas Funções podemos fazer leituras de arquivos excel e csv com libs
from funcoes_curso.leitura_arquivo import leitura_arquivos_excel, leitura_arquivos_csv
# As funções vão retornar um DataFrame
# Importando PandasGui para visualizarmos as colunas melhor
from pandasgui import show

'''
    LEIA ANOTAÇÃO: Uso do Help.txt
'''
# OBJETIVO AQUI É APENAS AMOSTRAR COMO O OBJETO HELP FUNCIONA

#print(help(leitura_arquivos_csv))
'''
SAIDA:

Help on function leitura_arquivos_csv in module funcoes_curso.leitura_arquivo:

leitura_arquivos_csv(nome_pasta, nome_arquivo_csv)

None
'''

#print(help(leitura_arquivos_excel))
'''
SAIDA:

Help on function leitura_arquivos_excel in module funcoes_curso.leitura_arquivo:

leitura_arquivos_excel(nome_pasta, nome_arquivo_excel)

None
'''
#print(help(show))
# Tem que fechar a interface do poandasgui par ao help() funcionar
'''
SAIDA -> Retorna informações sobre o objeto, módulo, função

    Help on PandasGui in module pandasgui.gui object:

Help on function show in module pandasgui.gui:

show(*args, settings: pandasgui.store.SettingsSchema = {}, **kwargs)
    Objects provided as args and kwargs should be any of the following:
    DataFrame   Show it using PandasGui
    Series      Show it using PandasGui
    Figure      Show it using FigureViewer. Supports figures from plotly, bokeh, matplotlib, altair, PIL
    dict/list   Show it using JsonViewer 
'''

# informações de assing
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_Compras.csv')
print(help(df.assign))
#  se aparecer -- Mais -- no final, precione Enter para mais informações
'''
SAIDA:

# Isso é próprio da função que eu criei
Caminho do arquivo CSV: C:\Estudando_pandas\Arquivos_csv_estudos\202401_Compras.csv
Arquivo CSV carregado com sucesso!

# Isso abaixo é do objeto Help()

Help on method assign in module pandas.core.frame:

assign(**kwargs) -> 'DataFrame' method of pandas.core.frame.DataFrame instance
    Assign new columns to a DataFrame.
    
    Returns a new object with all original columns in addition to new ones.
    Existing columns that are re-assigned will be overwritten.

-- Mais  -- #  Precione ENTER para mais informações

'''