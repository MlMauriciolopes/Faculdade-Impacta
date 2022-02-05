# -*- coding: utf-8 -*-
"""aula4_Data_Explolatory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X5twdEFoxxuUaZaLHgDfs45-qNj7Epmj
"""

import pandas as pd 
caminho_arquivo = '/content/drive/MyDrive/DNAC2017.csv'
sinasc = pd.read_csv(caminho_arquivo, dtype=str)
sinasc.PESO = pd.to_numeric(sinasc.PESO)
sinasc.SEMAGESTAC = pd.to_numeric(sinasc.SEMAGESTAC).astype(pd.Int64Dtype())
sinasc.IDADEMAE = pd.to_numeric(sinasc.IDADEMAE).astype(pd.Int64Dtype())

dados = sinasc[
               (sinasc.IDADEMAE < 18) &
               (sinasc.GRAVIDEZ == "2") &
               (sinasc.PESO.notna()) &
               (sinasc.SEMAGESTAC.notna())
]
dados

dados[['PESO','SEMAGESTAC']].corr()

# gráfico de dispersão 
import matplotlib.pyplot as plt
plt.scatter(dados.SEMAGESTAC, dados.PESO)

import numpy as np
# y = beta*x + alfa
beta, alfa = np.polyfit(dados.SEMAGESTAC.tolist(), dados.PESO.tolist(), deg=1)
plt.scatter(dados.SEMAGESTAC, dados.PESO)
plt.plot(dados.SEMAGESTAC, beta*dados.SEMAGESTAC + alfa,
         color="r", label = f'y = {round(alfa,2)} + {round(beta,2)} * x')
plt.legend(fontsize=14)
plt.show()

semanas = [30,31,32,33,34,35,36,37,38,39,40]
pesos = [beta*x + alfa for x in semanas]
pesos

# Exercício

# média de x - semanas de gestação
media_samanas = dados.SEMAGESTAC.mean()
#media de y - peso
media_peso = dados.PESO.mean()

numerador = sum((dados.SEMAGESTAC - media_samanas) * (dados.PESO - media_peso))
denominador = sum((dados.SEMAGESTAC - media_samanas)**2)
beta = numerador / denominador
beta

soma_n = 0
soma_d = 0
for i, d in dados[['SEMAGESTAC', 'PESO']].iterrows():  
  print(i)
  x = d[0] - media_semanas
  y = d[1] - media_peso
  x_y = x*y
  den = x**2
  soma_n += x_y
  soma_d += den
soma_n/soma_d

alfa = media_peso - beta* media_semanas
alfa