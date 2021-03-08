# covid_monitor
Este código 

### Dependências
- pandas
- matplotlib

### Como utilizar

Para utilizar o programa deve-se primeiro baixar os dados de contaminações por COVID do site do ministério da saúde. Para rodar o programa, siga os seguintes passos:
1) Acesse o site https://covid.saude.gov.br/
2) No canto superior direito, clique no botão "Arquivo CSV"
3) Salve o arquivo baixado no mesmo diretório do arquivo read_covid.py
4) Ajuste o nome no arquivo read_covid.py correspondente ao nome do arquivo CSV baixado.
5) Execute o programa

### Exemplo

```python
from read_covid import *

data = pd.read_csv("HIST_PAINEL_COVIDBR_07mar2021.csv",";")
cidades = ['São Paulo', 'Brasília']

fig, axis = plt.subplots(2, 2, figsize=(10,8))
plt.subplots_adjust(left=0.070, right=0.975, top=0.995, bottom=0.105, hspace=0.340, wspace=0.240)
plotCummulativeCases(cidades, data, axis[0][0], axis[0][1])
plotDailyCases(cidades, data, axis[1][0], axis[1][1])
plt.show()
```

produces

![](https://nschloe.github.io/perfplot/concat.svg)
