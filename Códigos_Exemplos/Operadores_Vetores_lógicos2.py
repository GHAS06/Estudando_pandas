import pandas as pd

'''
Nesse código vamos nos aperfeiçoar a filtragem através dos operadores com vetores 
lógicos.

Lembre-se: parenteses vai definir a operação do filtro e o limitador das filtragens
'''

caminho_arquivo_csv = r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_ItemCompra.csv"
df  = pd.read_csv(caminho_arquivo_csv, encoding= 'Latin1', sep = ';')

# puxando informações do arquivo csv
#print(df.info())

# Exibe o número de linhas e colunas do DataFrame
#print(df.shape)  

#print(df.head())

# exemplo: print(df.loc[[True,True,False],[True,False]])
                        
# Vetor lógico para as linhas: 11.989 linhas no DataFrame, selecionando as 3 primeiras
#linhas = [True, True, True] + [False] * (len(df) - 3)

# Vetor lógico para as colunas: 10 colunas no DataFrame, selecionando as 3 primeiras
#colunas = [True, True, True] + [False] * (len(df.columns) - 3)

# Seleção usando loc
#df_vetor_lógico = df.loc[linhas, colunas]

# Exibindo o resultado
#print(df_vetor_lógico)

'''
EXPLICAÇÃO DESTE CÓDIGO USANDO VETOR LÓGICO DETALHADAMENTE:



Contexto:
No seu código, você está usando vetores lógicos para realizar filtragens em um
DataFrame usando o método .loc[]. O .loc[] é uma maneira poderosa de acessar um
subconjunto de dados com base em linhas e colunas. Para isso, você utiliza listas 
de valores booleanos (True ou False), que servem para selecionar quais linhas e 
colunas serão mantidas na filtragem.

Vetores lógicos são listas de valores booleanos (ou seja, apenas True ou False), 
que podem ser usados para indicar quais linhas ou colunas de um DataFrame devem ser
selecionadas.

Um vetor lógico para linhas será uma lista de True e False, com a mesma quantidade 
de elementos que o número de linhas do DataFrame. Onde for True, a linha será 
selecionada; onde for False, a linha será excluída.

Um vetor lógico para colunas será uma lista de True e False, com a mesma quantidade
de elementos que o número de colunas do DataFrame. Onde for True, a coluna será
selecionada; onde for False, a coluna será excluída

No Python, a função len() é usada para obter o comprimento de um objeto, 
ou seja, o número de itens contidos nele. A função len() pode ser utilizada com
diferentes tipos de objetos, como listas, strings, tuplas, dicionários, entre outros.

Neste caso -> [False] * (len(df.columns) - 3)
Preenche o restante do vetor com False, até que o número total de elementos seja igual
ao número de colunas no DataFrame (10).

Depois de criar os vetores lógicos para as linhas e colunas, você usa o .loc[] 
para selecionar os dados.

O .loc[] aceita dois parâmetros:

O primeiro parâmetro (o vetor de linhas) seleciona as linhas.
O segundo parâmetro (o vetor de colunas) seleciona as colunas.

'''

# Usando Vetores lógicos com filtragem com operadores lógicos e selecionando colunas

#exemplo: print(df[(df.Nome == "Alice") & ((df.Idade == 25) | (df.Idade == 30))])

# fazendo filtragem com operador lógico, mas sem selecionar colunas específicas
print(df[(df['Código Órgão'] == 20301) & (df['Nome Órgão'] == 'Comissão Nacional de Energia Nuclear' )])

# fazendo filtragem com operadores lógicos e selecionando coluna específicas
print(df[(df['Código Órgão'] == 20301) & (df['Nome Órgão'] == 'Comissão Nacional de Energia Nuclear' )][['Quantidade Item','Valor Item']])

'''
Exeplicação: Do nosso Dataframe Selecionamos e filtramos a Coluna Código Órgão igual
a 20301 se verdadeiro vai retornar dados respectivos a essa coluna com esse código
e (and) selecionamos os dados do nosso DataFrame cujo a coluna Nome Órgão é igual a
Comissão Nacional de Energia Nucler, caso as duas colunas tenham valores lógicos True
irá retornar para gente os dados das colunas Quantidade Item e Valor Item do nosso 
Dataframe, porque com base nos operadores lógicos e se os dois dados forem verdadeiros
selecionamos aquelas duas colunas com seus respectivos dados com base no nosso filtro
com os operadores e vetores lógicos, abaixo coloquei a saida das dusa formas para entender

RESUMINDO: 
Se o Código Órgão igual a 20301 e Nome Órgão igual a Comissão Nacional de Energia Nucler
os dados que retornar no nosso DataFrame serão True, tanto para um como para outro.
Se for verdade isso, selecionaremos os dados das colunas Quantidade Item e Valor Item


Primeiro SAIDA(Apenas a filtragem com operadores lógicos):

INDEX      Código Órgão       Nome Órgão                  ...  Quantidade Item  Valor Item
0            20301  Comissão Nacional de Energia Nuclear  ...                1     8044,26
634          20301  Comissão Nacional de Energia Nuclear  ...               12    17933,43
637          20301  Comissão Nacional de Energia Nuclear  ...               12        0,00

Segunda SAIDA(Filtragem com operadores lógicos e selecionando colunas específicas):

INDEX  Quantidade Item  Valor Item
34                12    17933,43
637                12        0,00
640               123        0,00
643                 8        0,00
646               123     2566,54
1586          3361776        0,08
1592             6015      108,90
1595               72      126,60
2077                4     4500,00

'''