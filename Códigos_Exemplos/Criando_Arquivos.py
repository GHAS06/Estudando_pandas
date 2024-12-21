# Vamos aprender a criar  arquivos CSV (.csv) e Excel (.xlsx) usando o pandas
# Vim do futuro dizer que a mesma lógica deste código vai servir para o arquivo Excel

import pandas as pd
import numpy as np
import os
import time

# Criando um DataFrame através de um dicionário com Dados fictícios do setor administrativo
data = {
    "ID": range(1, 21),
    "Nome": [
        "Ana Silva", "Carlos Santos", "Mariana Costa", "José Oliveira", "Fernanda Lima",
        "Lucas Almeida", "Beatriz Moreira", "Rafael Souza", "Juliana Mendes", "Gabriel Ferreira",
        "Aline Rocha", "Thiago Martins", "Paula Barros", "Ricardo Campos", "Camila Batista",
        "Pedro Gonçalves", "Larissa Duarte", "Vinícius Teixeira", "Sofia Ribeiro", "Felipe Nascimento"
    ],
    "Departamento": np.random.choice(["RH", "Financeiro", "Logística", "TI"], 20),
    "Salário (R$)": np.random.randint(2500, 7000, 20),
    "Horas Trabalhadas/Semana": np.random.randint(20, 50, 20),
    "Anos de Experiência": np.random.randint(1, 15, 20),
    "Home Office": np.random.choice(["Sim", "Não"], 20),
}

df_administrativo = pd.DataFrame(data)

# Verificando dados do csv
print(df_administrativo.head())


# usando a função .to_csv() para converter o DataFrame em um arquivo.csv

df_administrativo.to_csv("Setor_Administrativo.csv", index = False) # index = False é para criar umm arquivo.csv sem indicie

# Usando os para  verificar onde o arquivo foi salva

# Usando os para verificar onde o arquivo foi salvo
caminho_origem = os.path.join(os.getcwd(), "Setor_Administrativo.csv")

# Determinando o caminho da pasta de Downloads
# Funciona em sistemas Windows, usando a variável de ambiente USERPROFILE
pasta_downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')

# Caminho de destino (onde o arquivo será movido)
caminho_destino = os.path.join(pasta_downloads, "Setor_Administrativo.csv")

# Movendo o arquivo para a pasta de Downloads
os.replace(caminho_origem, caminho_destino)

print(f"\nArquivo movido com sucesso para: {caminho_destino}\n")

# Lendo o arquivo csv gerado
# utilizando o index_col, define qual coluna deve ser usada como índice do DataFrame, ao invés de usar o índice numérico padrão (0, 1, 2, ...).
df_csv_gerado = pd.read_csv(caminho_destino, index_col = 0) 
print(df_csv_gerado.head(2)) # retornando as duas primeiras linhas

# removendo arquivo
print("\nAguarde 5s para o sistema remover o arquivo.csv\n")

start_time = time.time() 
for i in range(60, 0, -1):  # Começando de 5 e indo até 1
    print(f'Aguarde {i} segundos para remover o arquivo')
    time.sleep(1)  # Pausa de 1 segundo
end_time = time.time() 

real_time = end_time - start_time

# teste de segundos para ver se de fato demora 5 segundos para remoção
# print(f"\nDemorou tanto s para fazer isso {real_time}")
try:
    print("\nIniciando Remoção...") 
    time.sleep(2) 
    print("Removendo arquivo.csv..\n")
    time.sleep(2)
    os.remove(f'{caminho_destino}')
    print("Arquivo.csv removido com Sucesso")
except Exception as e:
    print(f"Erro durante a remoção do arquivo: {e}")

# O que é a variável de ambiente USERPROFILE? 

#   - No Windows, a variável de ambiente USERPROFILE contém o caminho para o diretório 
# principal do usuário.
#    Por exemplo, no seu sistema, ele pode ser algo como:

#    C:\Users\Proximo_analista 
#  modifiquei o caminho principal de usuário só para fins didáticos