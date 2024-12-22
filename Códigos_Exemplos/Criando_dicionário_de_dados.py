# Aqui o objetivo principal é mostrar formas de criar um diconário de dados com pandas
import sys 
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import pandas as pd
import numpy as np
from funcoes_curso.leitura_arquivo import leitura_arquivos_csv

# Para criarmos um diconário de dados, vamos primeiro criar um DataFrame com um dicionário
# do pandas contendo asa colunas chaves e os valores (especificações sobre a coluna)

# usando a função para crira uma DataFrame a partir de um csv
df = leitura_arquivos_csv('Arquivos_csv_estudos','202401_ItemCompra.csv')
print(df.head(2))

# pegando informações das colunas do nosso DataFrame
# basicamente o a função info() é um dicionário de dados.

print(df.info())

'''
SAIDA: 
    <class 'pandas.core.frame.DataFrame'>
RangeIndex: 11989 entries, 0 to 11988
Data columns (total 10 columns):
 #   Column                              Non-Null Count  Dtype
---  ------                              --------------  -----
 0   Código Órgão                        11989 non-null  int64
 1   Nome Órgão                          11989 non-null  object
 2   Código UG                           11989 non-null  int64
 3   Nome UG                             11989 non-null  object
 4   Número Contrato                     11989 non-null  int64
 5   Código Item Compra                  11989 non-null  object
 6   Descrição Item Compra               11989 non-null  object
 7   Descrição Complementar Item Compra  11989 non-null  object
 8   Quantidade Item                     11989 non-null  int64
 9   Valor Item                          11989 non-null  object
dtypes: int64(4), object(6)
memory usage: 936.8+ KB
'''

# Criando o nosso Dicionário de dados

dicionario_dados = {
    'Colunas':[
        'Código Órgão','Nome Órgão','Código UG','Nome UG','Número Contrato',
    'Código Item Compra','Descrição Item Compra','Descrição Complementar Item Compra',
    'Quantidade Item','Valor Item' ],
    'Descrção':[
        'Representa um identificador único numérico associado a um órgão público ou entidade administrativa',
        'Nome oficial do órgão ou entidade pública associada',
        'Código da Unidade Gestora (UG), que é responsável pela gestão administrativa e financeira do órgão',
        'Nome da Unidade Gestora, associado ao código UG. Fornece uma descrição textual da unidade específica dentro do órgão',
        'Identificador único para contratos registrados. Cada número representa um contrato firmado pelo órgão ou unidade gestora com fornecedores ou prestadores de serviços',
        'Código que identifica um item específico dentro do sistema de compras. Geralmente é alfanumérico e padronizado para rastrear produtos ou serviços adquiridos',
        'Descrição resumida do item ou serviço adquirido. Fornece informações básicas sobre o que está sendo comprado',
        'Informação adicional ou detalhamento do ite,m de compra. Pode incluir especificações técnicas, condições de fornecimento, ou características específicas do item',
        'Quantidade total do item adquirido no contrato. Representa a quantidade física ou o número de unidades adquiridas',
        'alor total monetário referente ao item adquirido, calculado com base na quantidade e no preço unitário. É representado na moeda do país (como reais no Brasil)'
        ],
    'Tipo_dado(incluindo_np)':[
        'int64', 'object', 'int64', 'object', 'int64', 'object',
        'object', 'object','int64','object',
        ]   
}

# Lembrando que você pode colocar outras informações que você achar relevante!
# Agora, vamos transformar esses dicionário de dados em um DataFrame!

dicionario_dados_completo = pd.DataFrame(dicionario_dados)

# depois de convertermos para um DataFrame, vamos converter para um arquivo csv ou excel 
# ou qualquer outro

print(dicionario_dados_completo)

dicionario_dados_completo.to_excel('Diconário_Dados_ItemCompras.xlsx')

# Pronto, nosso Dicionário de dados está completo, Agora no Excel você pode formatar a gosto

# montando automação de diretórios
try:
    print('\nMovendo arquivo...\n')
    time.sleep(2)
    caminho_origem = os.path.join(os.getcwd(),'Diconário_Dados_ItemCompras.xlsx')
    print(f'\ncaminho de origem: {caminho_origem}\n')
    
    # reaproveitando código, usando a variável de ambiente USERPROFILE para montar 
    # um caminho na pasta DOWNLOADS
    pasta_downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')

    # caminho de trasferência para pasta downloads
    caminho_destino = os.path.join(pasta_downloads,'Diconário_Dados_ItemCompras.xlsx')

    # Movendo o arquivo Excel, se existir
    if os.path.exists(caminho_origem):
        os.replace(caminho_origem, caminho_destino)
        print(f"Arquivo movido para: {caminho_destino}")
    else:
        print(f"Arquivo não encontrado em: {caminho_origem}")

except Exception as e:
    print(f'Aconteceu alguma cagada aqui: {e}')
