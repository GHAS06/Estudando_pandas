import pandas as pd
import numpy as np

# Esse estudo basea-se no curso gratuito do pandas que se encontra no Youtube
# Link para o curso: 

# Craindo Data Frame a partir de um dicionário para descobrir
# A quantidade de horas que ele possui https://www.youtube.com/watch?v=1ua6uksg6wg&list=PL4OAe-tL47sa1McMctk5pdPd5eTAp3drk&index=1

Aulas_YouTube = {

        'Vídeo_Aulas':[
            'Aula 0.0', 'Aula 0.1', 'Aula 0.2', 'Aula 0.3', 'Aula 0.4', 
        'Aula 0.5', 'Aula 0.6', 'Aula 0.7', 'Aula 0.8', 'Aula 0.9',
        'Aula 0.10', 'Aula 1.1', 'Aula 1.2', 'Aula 1.3', 'Aula 1.4',
        'Aula 1.5', 'Aula 1.6', 'Aula 1.7', 'Aula 1.8', 'Aula 1.9',
        'Aula 1.10', 'Aula 1.11', 'Aula 1.12', 'Aula 2.1', 'Aula 2.2',
        'Aula 2.3', 'Aula 2.4', 'Aula 3.1', 'Aula 3.2', 'Aula 3.3',
        'Aula 4.1', 'Aula 4.2', 'Aula 4.3', 'Aula 5.1', 'Aula 5.2', 
        'Aula 5.3', 'Aula 5.4'
            ],
        'Duração_Aulas':[
            3.54, 8.03, 7.15, 4.11, 5.31, 9.20, 10.04, 5.55, 13.13, 7.45, 
        11.12, 9.25, 8.16, 15.23, 14.29, 11.51, 13.23, 8.28, 8.04, 4.53, 
        10.06, 11.28, 8.33, 11.24, 11.29, 15.23, 10.28, 11.57, 7.49, 7.47, 
        13.34, 10.23, 15.32, 13.46, 13.52, 13.32, 15.20
        ]
}

# Materializando o Objeto DataFrame
df_aulas = pd.DataFrame(Aulas_YouTube)
#print(df_aulas)

#total_minutos = df_aulas['Duração_Aulas'].sum()
total_minutos = df_aulas.iloc[:,[1]].sum()
total_horas = (total_minutos / 60)

#Debugando
#print(total_horas)

horas = int(total_horas)  # Parte inteira das horas
minutos_restantes = round((total_horas - horas) * 60)  # Minutos restantes
#Debugando
#print(minutos_restantes[0])
print(type(minutos_restantes[0])) # saida -> numpy.float64
#print(type(minutos_restantes))
print(f'\nA duração total do curso é: {horas} horas e {minutos_restantes[0]} minutos.')
