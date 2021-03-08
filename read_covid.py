# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plotCity(city, ax1, ax2):
    nHabitantes = 1000
    
    ax1.plot(city['data'], nHabitantes*city['casosAcumulado']/city['populacaoTCU2019'], linewidth=2.0, label=city.municipio.iloc[0])
    ax1.grid(True)
    ax1.set_ylabel('Casos por 1000 habitantes', size=12)
    N = int(len(city['data'])/10)
    ax1.set_xticks(city['data'][::N])
    [tick.set_rotation(45) for tick in ax1.get_xticklabels()]
    
    ax2.plot(city['data'], nHabitantes*city['obitosAcumulado']/city['populacaoTCU2019'], linewidth=2.0, label=city.municipio.iloc[0])
    ax2.grid(True)
    ax2.set_ylabel('Óbitos por 1000 habitantes', size=12)
    N = int(len(city['data'])/10)
    ax2.set_xticks(city['data'][::N])
    [tick.set_rotation(45) for tick in ax2.get_xticklabels()]



if __name__ == '__main__':
    data = pd.read_csv("HIST_PAINEL_COVIDBR_07mar2021.csv",";")
    
    fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(10,5))
    plt.subplots_adjust(left=0.060, right=0.975, top=0.95, bottom=0.2)
    
    cidades = ['Ipuã', 'Florianópolis', 'São Paulo', 'Manaus', 'Brasília', 'São José do Rio Preto', 'Itajaí']
    
    # cidades = ['Brasília', 'Rio de Janeiro', 'Florianópolis', 'São Paulo', 'Curitiba', 'Itajaí', 'Porto Alegre', 'Blumenau']
    # cidades = ['Florianópolis', 'Itajaí', 'Chapecó', 'Brasília', 'Rio de Janeiro', 'São Paulo']

    # cidades = ['Cotia', 'Santos', 'Ipuã', 'Itatiba', 'São Luiz do Paraitinga', 'Florianópolis', 'São Paulo']
    for cidade in cidades:
        city = data.loc[data['municipio'] == cidade]
        plotCity(city, ax1, ax2)
    
    plt.legend(loc=0)
    plt.show()