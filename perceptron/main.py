import numpy as np
import matplotlib.pyplot as plt

from perceptron import Perceptron

# Dados de Treinamento
training_inputs = np.array([
  np.array([1.0, 2.0]),
  np.array([1.0, 1.0]),
  np.array([2.0, 1.0]),
  np.array([3.0, 3.0]),
  np.array([2.0, 3.0]),
  np.array([2.0, 2.5]),
])
labels = np.array([1, 1, 1, 0, 0, 0])
# 1: Vermelho
# 0: Preto

# Save grafic
x, y = training_inputs.T
c = np.array(['#FF0000' if l == 1 else '#000000' for l in labels])
plt.scatter(x, y, color=c)
plt.savefig('train.png')

# Perceptron com 2 entradas
perceptron = Perceptron(2)
# Treinamento
perceptron.train(training_inputs, labels)

## Test 1
inputs = np.array([0.5, 2.5])
predict = perceptron.predict(inputs)
print('## Teste 1')
print('Entrada: ', inputs)
if predict == 1:
  print('Previsão: Vermelho')
else:
  print('Previsão: Preto')
x, y = inputs.T
plt.scatter(x, y)
plt.savefig('predict-1.png')
#=> 1

## Test 2
inputs = np.array([3.5, 2.5])
predict = perceptron.predict(inputs)
print('## Teste 2')
print('Entrada: ', inputs)
if predict == 1:
  print('Previsão: Vermelho')
else:
  print('Previsão: Preto')
x, y = inputs.T
plt.scatter(x, y)
plt.savefig('predict-2.png')
#=> 0