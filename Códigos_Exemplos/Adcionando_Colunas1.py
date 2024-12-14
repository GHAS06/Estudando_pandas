import sys
import os

# Adiciona o diretório base ao sys.path
# Estava dando erro aqui, copiei do chat, estude essa lib sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora os imports devem funcionar
import pandas as pd
import numpy as np
from datetime import time
from funcoes_curso.leitura_arquivo import leitura_arquivos_excel

# Descomentar o que for necessário
''' 
    LEIA A ANOTAÇÃO: Abrindo_arquivos_com_lib1.txt
    LEIA A ANOTAÇÃO: Selecionando_colunas.txt
    LEIA A ANOTAÇÃO: A_importância_do_type()
    LEIA A ANOTAÇÃO: LOC_VS_ILOC.txt
    LEIA A ANOTAÇÃO: Manipulação_Colunas_DataFrame.txt
    LEIA A ANOTAÇÃO: Adicionando_Colunas_em_DaraFrames.txt
    VEJA O Código_Exemplo: data_frame4.py
'''

# Teste da função
#print(leitura_arquivos_excel('Arquivos_excel_para_estudos','produtos.xlsx'))

#print(type(leitura_arquivos_excel('Arquivos_excel_para_estudos','produtos.xlsx'))) 
# saida -> <class 'pandas.core.frame.DataFrame'>

# Adcionando Colunas através do nome da colunas (igual adcionar um valor em uma lista)
# essa adição está sendo relizada através da operação matématica de putras duas colunas

df = leitura_arquivos_excel('Arquivos_excel_para_estudos','produtos.xlsx')

#print(df.info()) # descobrir informações das colunas do DataFrame

# index            0         1
#lista_colunas = ['Preço','Estoque']

#df['Valor Total Vendas Produtos'] = df[lista_colunas[0]] * df[lista_colunas[1]]
#print(df)  

# Adcionando coluna via atributo através de um valor constante ou escalar
# quando fazemos isso, estamos fazendo explcidamente.

# Primeira forma de fazer isso, puxando o atriburo diretamente, não recomendada
#df.ID = 10
#print(df)

# Segunda forma, só que usando a função iloc, menos flexível
#df.iloc[:,5] = 10
#print(df)

# Terceira forma com função loc, mais criativa e flexível
#df.loc[0:5,'Valor Total Vendas Produtos'] = 50
#print(df)

# Quarta forma, mais recomendanda
#df['Valor Total Vendas Produtos'] = 40
#print(df)

#print(type(df['Valor Total Vendas Produtos']))

'''
    Basicamente estamos adcionando um novo atributo na coluna específicada, um bom
    exemplo é usando a função loc.

    df.loc[0:1,'Valor Total Vendas Produtos'] = 50
    print(df)

    SAIDA:
               ID    Produto    Categoria  Preço  Estoque  Valor Total Vendas Produtos
            0  101  Produto A  Categoria 1  25.50      200                         50.0
            1  102  Produto B  Categoria 2  30.00      150                         50.0
            2  103  Produto C  Categoria 1  15.75      300                         10.0
            3  104  Produto D  Categoria 3  60.50      100                         10.0
            4  105  Produto E  Categoria 2  45.00       50                         10.0


    Observe, irei mudar um pouco o parâmetro:

    df.loc[0:5,'Valor Total Vendas Produtos'] = 50
    print(df)

    SAIDA:
               ID    Produto    Categoria  Preço  Estoque  Valor Total Vendas Produtos
            0  101  Produto A  Categoria 1  25.50      200                         50.0
            1  102  Produto B  Categoria 2  30.00      150                         50.0
            2  103  Produto C  Categoria 1  15.75      300                         50.0
            3  104  Produto D  Categoria 3  60.50      100                         50.0
            4  105  Produto E  Categoria 2  45.00       50                         50.0

    LEMBRE-SE: Estamos modificando o DataFrame, mais na frente veremos sobre o copy,
    ou seja, toda modificação, estamos fazendo no Dataframe e não em uma cópia dele.
'''

# Adcionando Colunas via .append({dicionário_python_ou_função}, ignore_index = True)

# Primeira forma

#df_com_append = df._append({'Valor_Total_com_append':100},ignore_index=True)
#print(type(df._append({'Valor_Total_com_append':100},ignore_index=True))) 
# Saida -> Retorna um DataFrame 
#print(df_com_append)

# segunda forma, puxando uma coluna do DataFrame e armazenando numa variável

# Calculando a nova coluna
#df['Valor total Vendas Produto'] = df['Preço'] * df['Estoque']

# Selecionando a coluna como um DataFrame
# Armazenando a coluna em uma variável
# Lembre-se Selecionar a coluna como lista, no pandas vira um DataFrame
# Selecionando a coluna normalmente sem ser como lista, é uma series
#df_para_append = df[['Valor total Vendas Produto']].iloc[0]  # Selecionando a primeira linha da coluna como Série

# Adicionando a Série como nova linha no DataFrame
#df_com_append = df.append(df_para_append, ignore_index=True)

#print(df_com_append)

# Terceira forma usando a função ._append()

#Adcionando coluna através de operações aritiméticas de outras colunas
#df['Valor total Vendas Produto'] = df['Preço'] * df['Estoque']
# Transformando a coluna diretamente como um dicionário
#df_para_append = df[['Valor total Vendas Produto']]

#print(df_para_append) -> aqui retorna como um vetor do numpy
#print(type(df_para_append)) -> retorna dicionário

#df_com_append = df._append(df_para_append, ignore_index=True)
#print(df_com_append) # vai adcionar a coluna e o dados no final dela

'''
    Para usar o append, devemos fazer um dicionário com chave e valor, para contruir
    nossa coluna, muito boa para realizar mudanças específica.

    Essa abordagem funciona, mas tenha em mente que, no Pandas mais recente, o método
    append() é descontinuado e será removido no futuro. Caso esteja em uma versão
    atualizada, considere usar pd.concat() para melhor performance e compatibilidade
    futura.
'''

# Usando o pd.concat() para adcionar colunas

# Calculando a nova coluna
#df['Valor total Vendas Produto'] = df['Preço'] * df['Estoque']

# Armazenando a coluna em uma variável
#df_para_concat = df[['Valor total Vendas Produto']]  

# Adicionando a Série como nova linha no DataFrame usando pd.concat
#df_com_concat = pd.concat([df, df_para_concat], ignore_index=True)

#print(df_com_concat) # adiciona a coluna e os seus dados no final dela 

