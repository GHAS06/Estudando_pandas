import time
import requests
import pandas as pd

def dados_pokemon():

    # URL da API para pegar dados de todos os Pokémons
    api_pokemon_list = "https://pokeapi.co/api/v2/pokemon"
    
    # Lista para armazenar os nomes dos Pokémons
    pokemons = []

    # Dicionário para armazenar as informações de cada Pokémon
    pokemon_info = {
        "name": [],
        "height": [],
        "weight": [],
        "base_experience": [],
    }

    try:
        # Fazendo a requisição à API para obter a lista de Pokémons
        response = requests.get(api_pokemon_list)
        
        if response.status_code == 200:
            dados = response.json()
            
            # Adicionando os nomes dos Pokémons na lista
            for pokemon in dados['results']:
                pokemons.append(pokemon['name'])

            # Pegando todos os Pokémons, caso existam mais de uma página
            while dados['next']:
                response = requests.get(dados['next'])
                if response.status_code == 200:
                    dados = response.json()
                    for pokemon in dados['results']:
                        pokemons.append(pokemon['name'])
                else:
                    print("Erro ao pegar próxima página")
                    break

            print(f"Total de Pokémons encontrados: {len(pokemons)}")

        else:
            print(f"Erro ao pegar lista de Pokémons: {response.status_code}")

        # Iterando sobre a lista de Pokémons para pegar os dados de cada um
        for pokemon in pokemons:
           
            # URL da API para cada Pokémon
            api_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

            # Fazendo a requisição à API para pegar os dados de cada Pokémon
            response = requests.get(api_pokemon)
            
            print(f"Status Code: {response.status_code} - Pokémon: {pokemon}")

            if response.status_code == 200:
                # Convertendo a resposta JSON para um dicionário
                dados_pokemon = response.json()

                # Adicionando as informações relevantes ao dicionário
                pokemon_info["name"].append(dados_pokemon["name"])
                pokemon_info["height"].append(dados_pokemon["height"])
                pokemon_info["weight"].append(dados_pokemon["weight"])
                pokemon_info["base_experience"].append(dados_pokemon["base_experience"])
            else:
                print(f"Erro na requisição para {pokemon}: {response.status_code}")
        
        # Criando um DataFrame a partir do dicionário com os dados de múltiplos Pokémons
        df = pd.DataFrame(pokemon_info)
        print("\nDataFrame Criado com Sucesso!")
        return df 

    except Exception as e:
        print(f"Erro: {e}")

'''
    O .json() é fornecido pela biblioteca requests e é usado para converter 
    automaticamente o conteúdo da resposta (response) em um objeto Python equivalente,
    como um dicionário ou lista, dependendo da estrutura do JSON retornado.

    O que ele faz exatamente?
        
        Ele analisa o conteúdo da resposta como JSON (JavaScript Object Notation).
        Se a análise for bem-sucedida, retorna um objeto Python:
        Objeto JSON no formato de chave-valor → Dicionário Python (dict).
        Lista JSON → Lista Python (list).
        Se o conteúdo da resposta não for um JSON válido, ele gera uma exceção
        json.JSONDecodeError
'''
