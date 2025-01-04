# puxei esse arquivo csv deste site:

# https://basedosdados.org/dataset/96eab476-5d30-459b-82be-f888d4d0d6b9?table=bc84dea9-1126-4423-86d2-8835e6b19a72

# importando libs
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
        
from funcoes_curso.leitura_arquivo import leitura_arquivos_csv


pasta_arquivo_csv = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'br_inep_ideb_brasil.csv')

print()
print(pasta_arquivo_csv)

df = pd.read_csv(pasta_arquivo_csv, encoding='utf - 8',)

#show(df)

# informando dados de todas as tabelas: 
print()
print(df.info())

'''
 1   rede                         126 non-null    object
 2   ensino                       126 non-null    object
 3   anos_escolares               126 non-null    object

'''

'''
ano int64
'''

colunas_object = ['rede', 'ensino', 'anos_escolares']

for colunas_category in colunas_object:
    df[colunas_category] = df[colunas_category].astype('category')
    
df['ano'] = df['ano'].astype(np.int16)


print()
print(df.info())
print()
print(df.memory_usage())


'''
 4   taxa_aprovacao               126 non-null    float64 
 5   indicador_rendimento         126 non-null    float64 
 6   nota_saeb_matematica         126 non-null    float64 
 7   nota_saeb_lingua_portuguesa  126 non-null    float64 
 8   nota_saeb_media_padronizada  126 non-null    float64 
 9   ideb                         126 non-null    float64 
 10  ...
'''

colunas_float64 = [ 'taxa_aprovacao' , 'indicador_rendimento', 'nota_saeb_matematica', 'nota_saeb_lingua_portuguesa', 'nota_saeb_media_padronizada', 'ideb', 'projecao']
for colunas_float32 in colunas_float64:
    df[colunas_float32] = df[colunas_float32].astype(np.float32)


print()
print(df.info())

print()
print(df.memory_usage())


print()
print(df['projecao'].isnull().sum()) # 28 dados null


# no final o uso de memória do DataFrame é memory usage: 4.6 KB

# Fazendo uma descrição geral das colunas, após o tratamento de dados

print(df.describe(include = 'all'))

'''
                ano      rede       ensino  ... nota_saeb_media_padronizada        ideb   projecao
count    126.000000       126          126  ...                  126.000000  126.000000  98.000000
unique          NaN         5            2  ...                         NaN         NaN        NaN
top             NaN  estadual  fundamental  ...                         NaN         NaN        NaN
freq            NaN        27           90  ...                         NaN         NaN        NaN
mean    2013.000000       NaN          NaN  ...                    5.243896    4.673810   4.744898
std        5.184593       NaN          NaN  ...                    0.804800    1.069443   1.134021
min     2005.000000       NaN          NaN  ...                    4.064600    3.000000   3.100000
25%     2009.000000       NaN          NaN  ...                    4.546586    3.800000   3.825000
50%     2013.000000       NaN          NaN  ...                    5.112608    4.500000   4.600000
75%     2017.000000       NaN          NaN  ...                    5.955065    5.600000   5.500000
max     2021.000000       NaN          NaN  ...                    7.184233    7.100000   7.400000


Veja !

count: O número de valores não nulos.
unique: O número de valores únicos.
top: O valor mais frequente (moda).
freq: A frequência do valor mais frequente.

'''

# tranformando o dataframe em um arquivo xlsx e movendo para pasta downloads

'''
deixei comentado porque já fiz este procedimento

Arquivo_excel = df.to_excel("Inep_Ideb.xlsx", index = False)

try:
    caminho_origem = os.path.join(os.getcwd(),'Inep_Ideb.xlsx')
    print(f'\ncaminho de origem: {caminho_origem}\n')
    
    # usando a variável de ambiente USERPROFILE para montar 
    # um caminho na pasta DOWNLOADS
    pasta_downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')

    # caminho de trasferência para pasta downloads
    caminho_destino = os.path.join(pasta_downloads,'Inep_Ideb.xlsx')

    # Movendo o arquivo Excel, se existir
    if os.path.exists(caminho_origem):
        os.replace(caminho_origem, caminho_destino)
        print(f"Arquivo movido para: {caminho_destino}")
    else:
        print(f"Arquivo não encontrado em: {caminho_origem}\n")

except Exception as e:
    print(f'Aconteceu alguma cagada aqui: {e}')

'''

# vizualizando dados com pandasgui
#show(df)


# Vamos realizar uma análise de dados

'''
objetivo dessa análise é calcular a média geral da taxa de aprovação para o ensino médio
nas redes de ensino privada, pública e estadual, considerando os anos de 2005 a 2021.
'''

# criando filtro para obter apenas as linhas da rede pública, 
# podemos usar o método .isin() para faazer filtragem de linhas, mas obtei por fazer
# essa filtragem na mão

df_filtrado = df[
    ((df['rede'] == 'privada') |
     (df['rede'] == 'municipal') |
     (df['rede'] == 'estadual') |
     (df['rede'] == 'publica')) &
    (df['ensino'] == 'medio')
][['ano','rede','ensino','taxa_aprovacao']].sort_values(by='ano', ascending = False)

# lembre-se: | em pandas é ou e $ é and

print(df_filtrado)

'''
  ano      rede ensino  taxa_aprovacao
27  2021   privada  medio       98.500000
56  2021   publica  medio       89.800003
89  2021  estadual  medio       89.800003
34  2019   privada  medio       96.400002
83  2019  estadual  medio       84.500000
62  2019   publica  medio       84.699997
31  2017   privada  medio       95.699997
84  2017  estadual  medio       81.199997
55  2017   publica  medio       81.400002
30  2015   privada  medio       94.500000
87  2015  estadual  medio       79.699997
58  2015   publica  medio       79.800003
33  2013   privada  medio       93.800003
85  2013  estadual  medio       78.000000
60  2013   publica  medio       78.099998
59  2011   publica  medio       75.199997
35  2011   privada  medio       93.400002
86  2011  estadual  medio       75.000000
57  2009   publica  medio       73.699997
28  2009   privada  medio       93.300003
88  2009  estadual  medio       73.500000
61  2007   publica  medio       71.800003
81  2007  estadual  medio       71.599998
32  2007   privada  medio       93.800003
29  2005   privada  medio       92.699997
54  2005   publica  medio       70.599998
82  2005  estadual  medio       70.500000
'''

# com essa informação do filtro já descobrimos que o ensino médio não possui rede
# municipal

# fazendo o calculo da taxa_aprovação anula, somando todos e realizando uma média_geral

media_taxa_aprovacao = df_filtrado['taxa_aprovacao'].mean()


print()
print(f'A média geral é: {media_taxa_aprovacao:.2f}%')

'''
Agora vamos realizar um calculo que mostre a diferença entre a taxa de aprovação da rede
privada com as redes: estadual e publica de cada ano
'''


# Filtrando os dados apenas da rede privada para cada ano
df_privada = df_filtrado[df_filtrado['rede'] == 'privada'][['ano', 'taxa_aprovacao']]

# Renomeando a coluna para facilitar a associação posterior
df_privada = df_privada.rename(columns={'taxa_aprovacao': 'taxa_privada'})

# Realizando o merge para associar a taxa da rede privada com as outras redes para o mesmo ano
df_filtrado = df_filtrado.merge(df_privada, on='ano')


# Calculando a diferença entre a taxa da rede privada e as outras redes
df_filtrado['comparacao_rede_privada'] = (
    df_filtrado['taxa_privada'] -  df_filtrado['taxa_aprovacao']) 

# Exibindo o resultado
print(df_filtrado)

# fazendo uma gráfico com essa diferença

df_filtrado.plot(
    kind='bar', 
    x='ano', 
    y=['taxa_aprovacao', 'comparacao_rede_privada']
    )

# Adicionando título e rótulos
plt.title('Diferença da Taxa de Aprovação entre a Rede Privada e as Outras Redes (por Ano)', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Taxa de Aprovação (%)', fontsize=12)

# Exibindo o gráfico
plt.show()