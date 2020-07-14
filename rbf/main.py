import numpy as np
import matplotlib.pyplot as plt

from rbf import RBF

# Gerando 100 dados aleatórios
X = np.random.uniform(0., 1., 100)
X = np.sort(X, axis=0)
# Gerando a saída baseado nos dados aleatórios
# Seno de (2 * PI * X) + noise
noise = np.random.uniform(-0.1, 0.1, 100)
Y = np.sin(2 * np.pi * X)  + noise

# Criando e treinando a rede
learning_rate = 0.01 # Taxa de aprendizado
epochs = 100 # Epocas
k = 2 # Número de neurônios

rbf = RBF(k=k, learning_rate=learning_rate, epochs=epochs)
rbf.train(X, Y)

# Previsão
predictions = rbf.predict(X)

# Ploantdo dados de treinamento vs previsão
plt.plot(X, Y, '-o', label='train')
plt.plot(X, predictions, '-o', label='predict')
plt.legend()
 
plt.tight_layout()
plt.savefig('train-and-predict.png')