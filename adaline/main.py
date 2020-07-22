import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from adaline import Adaline

### Dados de Treinamento
# Um exemplo de rede Adaline para separar duas classes de flores Iris (Setosa e Versicolor) os dados para treinamento consistem em apenas 5 colunas (comprimento da pétala, largura da pétala, comprimento da sépala e largura da sépala, a última coluna é a classe da flor) e 35 amostras (linhas).
df = pd.read_csv('adaline/Dados_Treinamento_Sinal.csv', header=None)
df.head()

x = df.iloc[0:35,[0,1,2,3]].values
y = df.iloc[0:35,4].values


### Plotar o grafico
### vermelhos ----> Setosa (-1)
### azuis ----> Versicolor (1)
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
plt.scatter([sum(r) for index, r in df.iterrows()], x[:,3], c=y, cmap=cm_bright)
plt.scatter(None, None, color='r', label='Versicolor')
plt.scatter(None, None, color='b', label='Setosa')
plt.legend()
plt.title('Visualizacao do Dataset (flores Iris)')
plt.savefig('train.png')

# Adaline com 4 entradas
adaline = Adaline(4)
# Treinamento
adaline.train(x, y)

## Test 1
A = [0.4329,-1.3719,0.7022,-0.8535] # Versicolor (1)
predict = adaline.predict(A)
print('## Teste 1')
print('Entrada: ', A)
print('Classe esperada: Versicolor (1)')
if predict == 1:
  print('Previsão: Versicolor (1)')
else:
  print('Previsão: Setosa (-1)')
#=> 1

## Test 2
B = [0.3024,0.2286,0.8630,2.7909] # Setosa (-1)
predict = adaline.predict(B)
print('## Teste 2')
print('Entrada: ', B)
print('Classe esperada: Setosa (-1)')
if predict == 1:
  print('Previsão: Versicolor (1)')
else:
  print('Previsão: Setosa (-1)')
#=> 0


## Test #
C = [0.5971,1.4865,0.2904,4.6069] # Setosa (-1)
predict = adaline.predict(C)
print('## Teste 3')
print('Entrada: ', C)
print('Classe esperada: Setosa (-1)')
if predict == 1:
  print('Previsão: Versicolor (1)')
else:
  print('Previsão: Setosa (-1)')
#=> 0