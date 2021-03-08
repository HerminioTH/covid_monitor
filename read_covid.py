import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getMovingAvg(vector, periods=7):
    mvAvg = []
    for i in range(len(vector)):
        if i < periods:
            mvAvg.append(np.average(vector[:i]))
        else:
            mvAvg.append(np.average(vector[i-periods:i]))
    return np.array(mvAvg)

def plotCummulativeCases(cidades, data, ax1, ax2):
    for cidade in cidades:
        city_data = data.loc[data['municipio'] == cidade]
        nHabitantes = 1000

        ax1.plot(city_data['data'], nHabitantes*city_data['casosAcumulado']/city_data['populacaoTCU2019'], linewidth=2.0, label=city_data.municipio.iloc[0])
        ax1.grid(True)
        ax1.set_ylabel('Casos acumulados por 1000 hab.', size=12)
        N = int(len(city_data['data'])/10)
        ax1.set_xticks(city_data['data'][::N])
        [tick.set_rotation(45) for tick in ax1.get_xticklabels()]

        ax2.plot(city_data['data'], nHabitantes*city_data['obitosAcumulado']/city_data['populacaoTCU2019'], linewidth=2.0, label=city_data.municipio.iloc[0])
        ax2.grid(True)
        ax2.set_ylabel('Óbitos acumulados por 1000 hab.', size=12)
        N = int(len(city_data['data'])/10)
        ax2.set_xticks(city_data['data'][::N])
        [tick.set_rotation(45) for tick in ax2.get_xticklabels()]
    ax2.legend(loc=0, fancybox=True, shadow=True)

def plotDailyCases(cidades, data, ax1, ax2):
    for cidade in cidades:
        city_data = data.loc[data['municipio'] == cidade]
        nHabitantes = 1000

        daily_cases = np.array([today-yesterday for today, yesterday in zip(city_data['casosAcumulado'][1:], city_data['casosAcumulado'][:-1])])
        daily_deaths = np.array([today-yesterday for today, yesterday in zip(city_data['obitosAcumulado'][1:], city_data['obitosAcumulado'][:-1])])

        daily_cases = getMovingAvg(daily_cases, periods=15)
        daily_deaths = getMovingAvg(daily_deaths, periods=15)

        ax1.plot(city_data['data'][1:], nHabitantes*daily_cases/city_data['populacaoTCU2019'][1:], linewidth=2.0, label=city_data.municipio.iloc[0])
        # ax1.plot(city_data['data'][1:], daily_cases, linewidth=2.0, label=city_data.municipio.iloc[0])
        ax1.grid(True)
        ax1.set_ylabel('Casos diários por 1000 hab.', size=12)
        N = int(len(city_data['data'])/10)
        ax1.set_xticks(city_data['data'][1::N])
        [tick.set_rotation(45) for tick in ax1.get_xticklabels()]

        ax2.plot(city_data['data'][1:], nHabitantes*daily_deaths/city_data['populacaoTCU2019'][1:], linewidth=2.0, label=city_data.municipio.iloc[0])
        # ax2.plot(city_data['data'][1:], daily_deaths, linewidth=2.0, label=city_data.municipio.iloc[0])
        ax2.grid(True)
        ax2.set_ylabel('Óbitos diários por 1000 hab.', size=12)
        N = int(len(city_data['data'])/10)
        ax2.set_xticks(city_data['data'][1::N])
        [tick.set_rotation(45) for tick in ax2.get_xticklabels()]
    ax2.legend(loc=0, fancybox=True, shadow=True)

if __name__ == '__main__':
    data = pd.read_csv("HIST_PAINEL_COVIDBR_07mar2021.csv",";")
    cidades = ['Brasília', 'Florianópolis', 'São Paulo', 'Manaus', 'Brasília', 'Curitiba', 'Rio de Janeiro']
    cidades = ['Uberlândia', 'Ipuã', 'São José do Rio Preto']
    cidades = ['São Paulo', 'Brasília']

    fig, axis = plt.subplots(2, 2, figsize=(10,8))
    plt.subplots_adjust(left=0.070, right=0.975, top=0.995, bottom=0.105, hspace=0.340, wspace=0.240)
    plotCummulativeCases(cidades, data, axis[0][0], axis[0][1])
    plotDailyCases(cidades, data, axis[1][0], axis[1][1])
    plt.show()
