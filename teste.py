# -*- coding: utf-8 -*-
"""teste

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18hxUIpknNwOdbsmUhOjgN5JUEjy2RjVp
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv("Churn.csv", sep=";") #Chamando pelo nome o arquivo: dataset
dataset.head() #ler

dataset.shape #tamanho

dataset.columns = ["Id", "Score", "Estado", "Genero", "Idade", "Patrimonio", "Saldo", "Produtos", "TemCardCredito", "Ativo", "Salario", "Saiu"]
#dar nomes às colunas

dataset.head() #ler

agrupando = dataset.groupby('Estado').mean()

dataset.groupby(['Estado']).size()

dataset['Genero'].isnull().sum()

dataset['Idade'].describe()

plt.hist(Genero.iloc[:,3], bins=6)
plt.title('Genero')
plt.ylabel('Frequência')
plt.xlabel('Sexo')
