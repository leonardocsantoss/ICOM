import numpy as np

class Adaline(object):
  def __init__(self, no_of_inputs, epochs=100, learning_rate=0.001):
    self.epochs = epochs # Número de interacões
    self.learning_rate = learning_rate # Taxa de aprendizado
    np.random.seed(16)
    self.weights = np.random.uniform(-1, 1, no_of_inputs+1) # Pesos e o [0] é o bias
    self.error = [] # Taxa de erro

  def activation_function(self, inputs):
    # Calculo da saida da funcao g(z)
    return np.dot(inputs, self.weights[1:]) + self.weights[0]
    
  def predict(self, inputs):
    # Retornar valores binaros 1 ou -1
    return np.where(self.activation_function(inputs) >= 0.0, 1, -1)

  def train(self, training_inputs, labels):
    cost = 0
    # Para cada interação
    for _ in range(self.epochs):
      # Calcula a saída esperada
      output = self.activation_function(training_inputs)
      # Calcula o erro
      error = labels - output
      # Atualiza o bias baseado na taxa de aprendizado e no erro
      self.weights[0] += self.learning_rate * sum(error)
      # Atualiza os pesos
      self.weights[1:] += self.learning_rate * training_inputs.T.dot(error)
      # Adiciona o erro na lista de erros            
      cost = 1./2 * sum((error**2))
      self.error.append(cost)