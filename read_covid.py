import pandas as pd
import matplotlib.pyplot as plt

def plotCity(cidades, data, ax1, ax2):
    for cidade in cidades:
        city_data = data.loc[data['municipio'] == cidade]
        nHabitantes = 1000

        ax1.plot(city_data['data'], nHabitantes*city_data['casosAcumulado']/city_data['populacaoTCU2019'], linewidth=2.0, label=city_data.municipio.iloc[0])
        ax1.grid(True)
        ax1.set_ylabel('Casos por 1000 habitantes', size=12)
        N = int(len(city_data['data'])/10)
        ax1.set_xticks(city_data['data'][::N])
        [tick.set_rotation(45) for tick in ax1.get_xticklabels()]

        ax2.plot(city_data['data'], nHabitantes*city_data['obitosAcumulado']/city_data['populacaoTCU2019'], linewidth=2.0, label=city_data.municipio.iloc[0])
        ax2.grid(True)
        ax2.set_ylabel('Óbitos por 1000 habitantes', size=12)
        N = int(len(city_data['data'])/10)
        ax2.set_xticks(city_data['data'][::N])
        [tick.set_rotation(45) for tick in ax2.get_xticklabels()]

if __name__ == '__main__':
    data = pd.read_csv("HIST_PAINEL_COVIDBR_07mar2021.csv",";")
    cidades = ['Brasília', 'Florianópolis', 'São Paulo', 'Manaus', 'Brasília', 'Curitiba', 'Rio de Janeiro']

    fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(10,5))
    plt.subplots_adjust(left=0.060, right=0.975, top=0.95, bottom=0.2)
    plotCity(cidades, data, ax1, ax2)
    plt.legend(loc=0)
    plt.show()
