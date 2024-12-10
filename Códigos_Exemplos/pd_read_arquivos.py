import pandas as pd

# Descomente o que for necessário

# ler arquivo csv
#df = pd.read_csv(r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_Compras.csv",encoding='latin1',sep = ";", header=0, nrows=10, usecols=["Número do Contrato","Objeto","Fundamento Legal"])

# ler arquivos excel
#df = pd.read_excel(r, sheet_name= 0)"C:\Estudando_pandas\Arquivos_excel_para_estudos\Vendas.xlsx"

# Lendo arquivo excel usando ExcelFile e colocando isso em uma variável
#arquivo_excel = pd.ExcelFile(r"C:\Estudando_pandas\Arquivos_excel_para_estudos\Vendas.xlsx")

# exibindo as ABAS do arquivo.xlsx
#print(arquivo_excel.sheet_names)

# outra forma de selecionar e exibir abas do arquivo.xlsx
#ABA1 = arquivo_excel.parse("Multas-Novembro")
#ABA2 = arquivo_excel.parse("Protocolo-Novembro")

#print(ABA1, ABA2)

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
# exibindo informações dos dados e das colunas do dataframe
#print(df.info())

#exibindo e selecionando colunas específicas do dataframe
#print(df[["Número do Contrato","Objeto"]].head())
#print(df.Objeto.head())
