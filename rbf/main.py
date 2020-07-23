import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop

from rbf import RBFLayer, InitCentersKMeans

## Gerando 100 dados aleatórios
x = np.random.uniform(0., 1., 100)
x = np.sort(x, axis=0)
# Gerando a saída baseado nos dados aleatórios
# Seno de (2 * PI * X) + noise
noise = np.random.uniform(-0.1, 0.1, 100)
y = np.sin(2 * np.pi * x) + noise
# Organizando os dados
x = np.column_stack((x, ))
y = np.column_stack((y, ))

## Criando e treinando a rede
epochs = 2000 # Epocas
k = 10 # Número de neurônios da camada escondida
input_dim = len(x[0]) # Número de entradas
output_size = 1 # Número de neurôniso de saída

# Modelo
model = Sequential()
model.add(RBFLayer(k, initializer=InitCentersKMeans(x), betas=2.0, input_shape=(input_dim, )))
model.add(Dense(output_size, use_bias=False))
model.compile(loss='mean_squared_error', optimizer=RMSprop())

model.fit(x, y, batch_size=50, epochs=epochs)

# Previsão
predictions = model.predict(x)

# Ploantdo dados de treinamento vs previsão
plt.plot(range(len(y)), y, '-o', label='train')
plt.plot(range(len(y)), predictions, '-o', label='predict')
plt.legend()
 
plt.tight_layout()
plt.show()