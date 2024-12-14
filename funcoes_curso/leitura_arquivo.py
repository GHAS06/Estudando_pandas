import pandas as pd
import os

# Função para leitura de arquivos CSV
def leitura_arquivos_csv(nome_pasta,nome_arquivo_csv):
    # Diretório base
    diretorio_base = os.getcwd()

    # Construindo o caminho correto
    caminho_arquivo = os.path.join(diretorio_base, 'Arquivos_csv_estudos', nome_arquivo_csv)

    # Verifique o caminho gerado
    print("Caminho do arquivo CSV:", caminho_arquivo)

    # Tente carregar o arquivo
    try:
        df = pd.read_csv(caminho_arquivo, encoding="latin1", sep=';')
        print("Arquivo CSV carregado com sucesso!")
        return df

    except FileNotFoundError:
        print(f"Erro: Arquivo CSV '{nome_arquivo_csv}' não encontrado no caminho '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

    # Retorna None em caso de erro
    return None

#Função para leitura de arquivos Excel
def leitura_arquivos_excel(nome_pasta,nome_arquivo_excel):
    # Diretório base
    diretorio_base = os.getcwd()
    #print(diretorio_base) #debugando
    # Construindo o caminho correto
    caminho_arquivo = os.path.join(diretorio_base, nome_pasta, nome_arquivo_excel)

    # Verifique o caminho gerado
    print("Caminho do arquivo Excel:", caminho_arquivo)

    # Tente carregar o arquivo
    try:
        df = pd.read_excel(caminho_arquivo)
        print("Arquivo Excel carregado com sucesso!")
        return df

    except FileNotFoundError:
        print(f"Erro: Arquivo Excel '{nome_arquivo_excel}' não encontrado no caminho '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")

    # Retorna None em caso de erro
    return None

#Debugando
#print(leitura_arquivos_excel('Arquivos_excel_para_estudos','produtos.xlsx'))
