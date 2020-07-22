import tensorflow.compat.v1 as tf
import numpy as np

tf.disable_v2_behavior()

class MLP2Layers():
    def __init__(self, learning_rate=0.01, training_epochs=5000, n_input=4, n_hidden=10, n_output=3):
        self.learning_rate = learning_rate # Taxa de aprendizado
        self.training_epochs = training_epochs # Epoca
        self.n_input = n_input #quantos valores de entrada?
        self.n_hidden = n_hidden #quantos neurônios na camada oculta?
        self.n_output = n_output #quantos neuronios na camada de saida?

        # Inicializa os pessos com valores aleatórios
        self.weights = {
            "hidden": tf.Variable(tf.random_normal([self.n_input, self.n_hidden])),
            "output": tf.Variable(tf.random_normal([self.n_hidden, self.n_output])),
        }
        # Inicializa os bias com valores aleatórios
        self.bias = {
            "hidden": tf.Variable(tf.random_normal([self.n_hidden])),
            "output": tf.Variable(tf.random_normal([self.n_output])),
        }

        # Função de ativação do
        def model(X, weights, bias):
            layer1 = tf.add(tf.matmul(X, weights["hidden"]), bias["hidden"])
            layer1 = tf.nn.relu(layer1)

            output_layer = tf.matmul(layer1, weights["output"]) + bias["output"]
            return output_layer

        # Placeholder da entrada de acordo com o número de entrada
        self.X = tf.placeholder("float",[None, self.n_input])
        # Placeholder da saída de acordo com o número de saída
        self.Y = tf.placeholder("float",[None, self.n_output])

        # Função de ativação
        self.pred = model(self.X, self.weights, self.bias)
        # Função de custo
        self.cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.pred, labels=self.Y))
        # Função de otimização
        self.optimizador = tf.train.AdamOptimizer(self.learning_rate).minimize(self.cost)
        # Inicializa uma sessão
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)

    def train(self, train_X, train_Y, test_X, test_Y):
        # Método de treinamento
        for epochs in range(self.training_epochs):
            _, c= self.sess.run([self.optimizador, self.cost], feed_dict = {self.X: train_X, self.Y: train_Y})
            if(epochs + 1) % 100 == 0: # Só imprime de 100 em 100
                print("Epoch:", epochs+1, "Cost:", c)
        print("Optimization Finished")

        test_result = self.sess.run(self.pred, feed_dict = {self.X: train_X})
        correct_prediction = tf.equal(tf.argmax(test_result, 1), tf.argmax(train_Y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print("accuracy:", accuracy.eval({self.X: test_X, self.Y: test_Y}, session=self.sess))
    
    def test(self, test_X, test_Y):
        test_result = self.sess.run(self.pred, feed_dict = {self.X: test_X})
        correct_prediction = tf.equal(tf.argmax(test_result, 1), tf.argmax(test_Y, 1))
        return correct_prediction.eval(session=self.sess)