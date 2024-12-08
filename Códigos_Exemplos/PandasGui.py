import pandas as pd
from pandasgui import show

caminho_arquivo_csv = r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_ItemCompra.csv"
df  = pd.read_csv(caminho_arquivo_csv, encoding= 'Latin1', sep = ';')

show(df)

'''
Recomendações de Uso do Pandas e PandasGui:

PandasGui: É altamente recomendado para manipular grandes quantidades de dados,
pois ele oferece uma interface gráfica para visualização e edição de DataFrames. 
No entanto, como ele carrega os dados na interface gráfica, pode levar algum tempo
para abrir, especialmente com conjuntos de dados muito grandes.
Portanto, embora o PandasGui facilite a análise e manipulação interativa,
ele pode não ser a melhor opção quando você precisa de resultados rápidos em grandes
volumes de dados.

Pandas (no terminal): É a melhor opção quando você precisa de manipulações rápidas e 
eficientes diretamente no terminal ou em um ambiente de desenvolvimento, como
o Jupyter Notebook ou o Visual Studio Code. O Pandas é muito rápido e eficaz para 
realizar tarefas de processamento de dados sem a sobrecarga de uma interface gráfica,
sendo ideal para tarefas automatizadas ou quando o desempenho é a prioridade.
'''