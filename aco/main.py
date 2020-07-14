import random

from aco import SolveTSPUsingACO


## Gerando cidades aleatórias
cities_size = 15
nodes = [(random.uniform(-400, 400), random.uniform(-400, 400)) for i in range(cities_size)]


## Definindo parametros do ACO
colony_size = 10 # Número de formigas
steps = 100 # Número de interações
alpha = 1.0 # Se α = 0, só há influência da distância, assim seria algo como a busca gulosa
beta = 3.0 # Se β = 0 existe somente a dependência do feromônio, encontrando rotinas fortemente sub-ótimas
mode = 'ACS' # Tipo de Algoritmo. Possibilidades: ACS, Elitist, MaxMin

# Instanciando o ACO
acs = SolveTSPUsingACO(mode=mode, colony_size=colony_size, steps=steps, alpha=alpha, beta=beta, nodes=nodes)

# Rodando o ACO
acs.run()

# Plotando o ACO
acs.plot()