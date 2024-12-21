# Vamos entender como funciona o endereçamento de memória utilizando o sys.path
#  da biblioteca sys.

# O sys.path é uma lista que contém todos os diretórios onde o interpretador
#  Python pode procurar por módulos.

# Lembre-se:

# - O sys.path é uma LISTA e pode ser manipulada como qualquer outra lista no Python.
# - Ele inclui caminhos como o diretório atual, os diretórios padrão do Python, e os
#  definidos na variável PYTHONPATH.

# Exemplo: Mostrar todos os caminhos no sys.path

import sys

# Listar os métodos que listas (e sys.path) possuem
print(dir(sys.path))  # Isso mostrará métodos como append, extend', etc.
print()
# Mostrar todos os diretórios onde o Python procura módulos
for idx, path in enumerate(sys.path):
    print(f"{idx}: {path}")

# Adicionando um novo caminho ao sys.path
novo_caminho = "/meu/novo/caminho"
if novo_caminho not in sys.path:
    sys.path.append(novo_caminho)
    print(f"\nNovo caminho adicionado: {sys.path[-1]}") # fazendo o slice do último item da lista

# Removendo um caminho
if novo_caminho in sys.path:
    sys.path.remove(novo_caminho)
    print(f"\nCaminho removido: {novo_caminho}\n")
