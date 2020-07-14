from mlp import MLP2Layers

# Como nosso dataset contem string na coluna Y (classes) faremos uma substituicao (encode) da string por um vetor
def label_encode(label):
    if label == "Iris-setosa":
        return [1,0,0]
    elif label == "Iris-versicolor":
        return [0,1,0]
    elif label == "Iris-virginica":
        return [0,0,1]

def label_decode(val):
    if val == [1,0,0]:
        return "Iris-setosa"
    elif val == [0,1,0]:
        return "Iris-versicolor"
    elif val == [0,0,1]:
        return "Iris-virginica"

def data_encode(file):
    X = []
    Y = []
    train_file = open(file, 'r')
    for line in train_file.read().strip().split('\n'):
        line = line.split(',')
        X.append([line[0],line[1],line[2],line[3]])
        Y.append(label_encode(line[4]))
    return X,Y


train_X, train_Y = data_encode("iris.train") #dataset de treinamento
test_X, test_Y = data_encode("iris.test") #dataset de validacao


learning_rate = 0.01  # Taxa de aprendizado
training_epochs = 5000  # Epoca
n_input = 4  #quantos valores de entrada?
n_hidden = 10  #quantos neurônios na camada oculta?
n_output = 3  #quantos neuronios na camada de saida?

mlp = MLP2Layers(learning_rate, training_epochs, n_input, n_hidden, n_output)
mlp.train(train_X, train_Y, test_X, test_Y)

# Teste um a um
for i in range(len(test_X)):
    t_X = test_X[i]
    t_Y = test_Y[i]
    l_Y = label_decode(t_Y)

    result = mlp.test([t_X], [t_Y])
    print('Dados de entrada: ', t_X)
    print('Valor esperado: ', l_Y)
    print('Valor encontrado corretamente: ', result[0], '\n')