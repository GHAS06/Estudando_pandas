import pandas as pd

# Esse código visa aprofundar mais um pouco sobre Renomeação e tratamenot de colunas
# iremos fazer isso utilizando columns

'''
    LEIA A ANOTAÇÃO: Renomeando_Colunas1.txt
    LEIA A ANOTAÇÃO: Renomeando_Colunas2.txt

    
    IMPORTANTE -> Se deseja realziar modificações nas colunas e quiser ser mais 
    seguro, use a função .rename(), agora Se você precisa modificar os nomes das 
    colunas diretamente (sem criar um novo objeto), 
    use df.columns = [...], como foi feito nos exemplos com list comprehension.
'''

dados = {
        'Nome': ['Ana', 'Carlos', 'João', 'Maria', 'Lucas'],
        'Idade': [23, 35, 28, 42, 19],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba'],
        'Profissão': ['Analista', 'Desenvolvedor', 'Gerente', 'Designer', 'Estagiário'],
        'Salário Pagamento': [3500, 5000, 8000, 4500, 1500]
    }

df = pd.DataFrame(dados)

print(df.columns) 
print(type(df.columns)) 

# Exemplo de Tratamento de colunas com list comprehension

# list comprehensio com for loop
df.columns = [x.replace(' ', '_') for x in df.columns.to_list()]
#print(df)

# Usando list comprehension com if para substituir espaços por underscores, 
# mas somente nas colunas que contêm 'Pagamento'
df.columns = [coluna.replace(' ', '_') if 'Pagamento' in coluna else coluna for coluna in df.columns]
print(df)

# Usando funções de manipulação stirng para colocar todos os nomes das colunas  em Maiúsculo
df.columns = [x.replace(' ', '_') for x in df.columns.to_list()]
print(df)