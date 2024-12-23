# Vamos Gerar um dicionário de dados do DataFrame gerado atrvés da API do pokemon

# importando libs
import sys
import os
import time
import requests 
import pandas as pd

try:

    # fazendo um caminho absoluto para o interpretador python ler
    sys.path.append(os.path.abspath(os.path.join(os.getcwd())))

    # puxando o ultimo item da lista de módulos lida pelo interpretador
    print(sys.path[-1])

except Exception as e:
    print(f"Erro: {e}")

from funcoes_curso.pokemon_api_dados import dados_pokemon

# puxando os dados da API e retornando com um DataFrame
DataFrame = dados_pokemon()

# puxando informações sobre os tipos de dados das  colunas 
print(DataFrame.info())

# dicionário para
dicio_dados_pokemon = {
    'Colunas':['name','height','weight','base_experience'],
    'Descrição':[
        'Nome do Pokémon. Identifica de forma única cada Pokémon dentro do conjunto de dados.',
        'Altura do Pokémon, normalmente medida em decímetros (dm). Pode ser usada para comparações físicas entre os Pokémon.',
        'Peso do Pokémon, normalmente medido em hectogramas (hg). Usado para análise de tamanho e proporção.',
        'Experiência base que um Pokémon fornece ao ser derrotado em batalhas. Mede o quanto ele contribui para o treinamento de outros Pokémon.'
        ],
    'Tipo_dados':['object','int64','int64','int64']
}

# transformar transformar o diconário do dicio_dados_pokemon em um DataFrame
Dicionário_Dados = pd.DataFrame(dicio_dados_pokemon)

# Transformando o dicionário em um arquivo excel, será salvo neste repositório
Dicionário_Dados.to_excel('Dicionário_dados_DataFrame_Pokemon.xlsx')

try:
    # caminho que o arquivo está 
    caminho_origem = os.path.join(os.getcwd(),'Dicionário_dados_DataFrame_Pokemon.xlsx')
    
    #debugando
    print(f'\ncaminho_origem: {caminho_origem}\n')    
    
    # caminho para qual vou mover o arquivo
    caminho_destino = os.path.join(os.getcwd(),'Dicionário_dados','Dicionário_dados_DataFrame_Pokemon.xlsx')
    
    # debugando
    print(f'caminho_destino: {caminho_destino}\n')
    
    print("Movendo o arquivo...")
    time.sleep(2)
    
    # movendo o arquivo para a pasta Dicionário
    os.replace(caminho_origem, caminho_destino)
    print('Arquivo movido com Sucesso!')

except Exception as e:
    print(f"Aconteceu alguma cagada aqui: {e}")