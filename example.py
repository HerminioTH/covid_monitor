from read_covid import *

data = pd.read_csv("HIST_PAINEL_COVIDBR_07mar2021.csv",";")
cidades = ['São Paulo', 'Brasília']

fig, axis = plt.subplots(2, 2, figsize=(10,8))
plt.subplots_adjust(left=0.070, right=0.975, top=0.995, bottom=0.105, hspace=0.340, wspace=0.240)
plotCummulativeCases(cidades, data, axis[0][0], axis[0][1])
plotDailyCases(cidades, data, axis[1][0], axis[1][1])
plt.show()
