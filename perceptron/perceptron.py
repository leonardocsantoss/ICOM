import numpy as np

class Perceptron(object):

  def __init__(self, no_of_inputs, ephocas=100, learning_rate=0.01):
    self.ephocas = ephocas # Número de interacões
    self.learning_rate = learning_rate # Taxa de aprendizado
    self.weights = np.zeros(no_of_inputs) # Pesos
    self.bias = 0.0 # Bias
           
  def predict(self, inputs):
    # Multiplica peso * input e soma tudo
    # Adiciona ao final o bias
    summation = np.dot(inputs, self.weights) + self.bias
    if summation > 0:
      return 1
    else:
      return 0

  def train(self, training_inputs, labels):
    # Para cada interação
    for _ in range(self.ephocas):
      # Junta a entra e a saída
      for inputs, label in zip(training_inputs, labels):
        # Faz a previsão
        prediction = self.predict(inputs)
        # Atualiza os pesos
        self.weights += self.learning_rate * inputs * (label - prediction)
        # Atualiza o bias
        self.bias += self.learning_rate * (label - prediction)