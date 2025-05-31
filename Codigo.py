## Este exemplo replica a distribuição binomial ao jogar uma moeda 500 vezes.



# Biblioteca que importamos.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# Parametros que serão utilizados.
n = 500 #Indica a variavél N.
p = 0.5 #Indica a probabilidade.
x = np.arange(0, n+1)
binomal = binom.pmf(k=x, n=n, p=p)

#Criação e exibição do gráfico.
plt.plot(x, binomal) #Cria grafico de linha.
plt.xlabel("X", fontsize=10) #Indica o nome dado ao eixo X e determina o tamanho da fonte.
plt.ylabel("Probabilidade", fontsize=10) #Indica o nome dado ao eixo Y e determina o tamanho da fonte.
plt.xlim([0, n])
plt.title("Distribuição Binominal. n={0}, p={1}".format(n, p), fontsize= 14) #Determina o Titulo do gráfico, fazendo menção à quantidade de tentativas e à probabilidade.
plt.show()
