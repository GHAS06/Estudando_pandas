# importando libs
import sys
import os
import time
import pandas as pd
import numpy as np

try:
    # realizando testes para saber qual diretório estou
    print(os.getcwd())

    # fazendo um caminho absoluto para o interpretador python ler
    sys.path.append(os.path.abspath(os.path.join(os.getcwd())))

    # puxando o ultimo item da lista de módulos lida pelo interpretador
    print(sys.path[-1])

except Exception as e:
    print(f"Erro: {e}")
        
from funcoes_curso.leitura_arquivo import leitura_arquivos_excel

# realizando caminho para o arquivo csv
pasta_arquivo_excel = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'Inep_Ideb.xlsx')

# lendo o arquivo csv e retornando um DataFrame
df = pd.read_excel(pasta_arquivo_excel)

# leva em consideração que este dicionário vai está com as colunas tratadas
print(df.head())


# Contruindo o nosso dicionário de dados
dicionario_dados = {
    "ano": {
        "Descrição": "Ano de referência para os dados analisados no conjunto.",
        "Tipo": "int16",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Anos representados no dataset, como 2015, 2017, etc.",
        "Observação": "Indica o ano em que os indicadores educacionais foram coletados ou calculados."
    },
    "rede": {
        "Descrição": "Rede de ensino que fornece a educação (e.g., municipal, estadual, federal).",
        "Tipo": "category",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores categóricos como 'Estadual', 'Municipal', 'Federal'.",
        "Observação": "Classifica as escolas conforme a administração pública responsável por elas."
    },
    "ensino": {
        "Descrição": "Etapa do ensino referente ao indicador (e.g., fundamental, médio).",
        "Tipo": "category",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores categóricos como 'Ensino Fundamental', 'Ensino Médio'.",
        "Observação": "Identifica a etapa de ensino associada aos dados."
    },
    "anos_escolares": {
        "Descrição": "Agrupamento dos anos escolares considerados na análise.",
        "Tipo": "category",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Categorias como '1º ao 5º ano', '6º ao 9º ano'.",
        "Observação": "Define o grupo de anos escolares com base no ciclo educacional."
    },
    "taxa_aprovacao": {
        "Descrição": "Porcentagem de alunos aprovados em relação ao total matriculado.",
        "Tipo": "float32",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores contínuos entre 0 e 100, representando porcentagens.",
        "Observação": "Avalia o desempenho em termos de aprovação dos alunos."
    },
    "indicador_rendimento": {
        "Descrição": "Métrica que avalia o rendimento escolar dos alunos.",
        "Tipo": "float32",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores contínuos representando o nível de rendimento (0 a 100).",
        "Observação": "O rendimento é calculado a partir de indicadores de desempenho."
    },
    "nota_saeb_matematica": {
        "Descrição": "Nota média obtida pelos alunos na avaliação de matemática aplicada pelo SAEB.",
        "Tipo": "float32",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores contínuos, geralmente entre 0 e 500.",
        "Observação": "A nota é padronizada para comparação nacional em matemática."
    },
    "nota_saeb_lingua_portuguesa": {
        "Descrição": "Nota média obtida pelos alunos na avaliação de língua portuguesa aplicada pelo SAEB.",
        "Tipo": "float32",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores contínuos, geralmente entre 0 e 500.",
        "Observação": "A nota é padronizada para comparação nacional em língua portuguesa."
    },
    "nota_saeb_media_padronizada": {
        "Descrição": "Média padronizada das notas de matemática e língua portuguesa do SAEB.",
        "Tipo": "float32",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores contínuos, geralmente entre 0 e 500.",
        "Observação": "A média combina os desempenhos em matemática e língua portuguesa."
    },
    "ideb": {
        "Descrição": "Índice de Desenvolvimento da Educação Básica (IDEB).",
        "Tipo": "float32",
        "Valores Não Nulos": 126,
        "Valores Possíveis": "Valores contínuos que variam por etapa de ensino e ano.",
        "Observação": "O IDEB é calculado combinando taxas de aprovação e desempenho no SAEB."
    },
    "projecao": {
        "Descrição": "Estimativa futura para o IDEB, baseada em tendências observadas.",
        "Tipo": "float32",
        "Valores Não Nulos": 98,
        "Valores Possíveis": "Valores contínuos, mas pode conter valores nulos (28 dados ausentes).",
        "Observação": "Projeção estatística baseada no histórico de dados educacionais."
    }
}

# Criando arquivo xlsx fdo dicionário de dados

dicio_data = pd.DataFrame(dicionario_dados)

arquivo_excel = dicio_data.to_excel('Dicionário_inep_ideb.xlsx')
try:
    # caminho que o arquivo está 
    caminho_origem = os.path.join(os.getcwd(),'Dicionário_inep_ideb.xlsx')
    
    #debugando
    print(f'\ncaminho_origem: {caminho_origem}\n')    
    
    # caminho para qual vou mover o arquivo
    caminho_destino = os.path.join(os.getcwd(),'Dicionário_dados','Dicionário_inep_ideb.xlsx')
    
    # debugando
    print(f'caminho_destino: {caminho_destino}\n')
    
    print("Movendo o arquivo...")
    time.sleep(2)
    
    # movendo o arquivo para a pasta Dicionário
    os.replace(caminho_origem, caminho_destino)
    print('Arquivo movido com Sucesso!')

except Exception as e:
    print(f"Aconteceu alguma cagada aqui: {e}")