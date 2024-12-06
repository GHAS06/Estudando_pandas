import pandas as pd

# ler arquivo csv
df = pd.read_csv(r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_Compras.csv",encoding='latin1',sep = ";", nrows=100)

# ler arquivos excel
#df = pd.read_excel("/caminho/arquivo.xlsx")

# ler arquivos json,
#df = pd.read_json("/caminho/arquivo.json")

# com sqlalquemy podemos ler arquivos sql com pandas

'''
import pandas as pd from sqlalchemy import create_engine

# Criar a engine de conexão 
engine = create_engine('mysql+pymysql://usuario:senha@host:porta/nome_do_banco') 

# Consulta SQL 
query = "SELECT * FROM sua_tabela" 

# Ler dados do SQL para o DataFrame
df_sql = pd.read_sql(query, engine) # Exibir o DataFrame
'''

