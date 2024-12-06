import pandas as pd 

dados = {
            
    "Produtos":['A','B','C'],
    "Quantidade":[10,20,30],
    "Preço":[5.0,10.0,15.0]
                    }

df = pd.DataFrame(dados)
#df['Total'] = df['Quantidade'] * df['Preço'] adcionaando coluna total

#df.rename(columns={'Produtos': 'Itens'}, inplace=True) renomeia colunas
print(df)

#print(df.to_string(index=False))
#print(df.iloc[0])

#print(df['Produtos'])

#print(df[df['Quantidade'] > 10])