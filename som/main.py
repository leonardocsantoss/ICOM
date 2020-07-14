import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from minisom import MiniSom
from sklearn.preprocessing import scale


# https://en.wikipedia.org/wiki/Democracy_Index
# The Democracy Index is an index compiled by the Economist Intelligence Unit (EIU), a UK-based company. Its intention is to measure the state of democracy in 167 countries, of which 166 are sovereign states and 164 are UN member states.
# The index was first published in 2006, with updates for 2008, 2010 and later years. The index is based on 60 indicators grouped in five different categories, measuring pluralism, civil liberties and political culture. In addition to a numeric score and a ranking, the index categorises each country in one of four regime types: full democracies, flawed democracies, hybrid regimes and authoritarian regimes.
# Carregando o dataset
democracy_index = pd.read_csv('democracy_index.csv')

# Definindo cores
category_color = {'Full democracy': 'darkgreen',
                  'Flawed democracy': 'limegreen',
                  'Hybrid regime': 'darkorange',
                  'Authoritarian': 'crimson'}
colors_dict = {c: category_color[dm] for c, dm in zip(democracy_index.country, democracy_index.category)}

# Buscando apenas 6 colunas no dataset e normalizando os dados
X = democracy_index[['democracy_index', 'electoral_processand_pluralism', 'functioning_of_government', 'political_participation', 'political_culture', 'civil_liberties']].values
X = scale(X)

# Definindo um SOM 15x15
size = 100
som = MiniSom(size, size, len(X[0]),
              neighborhood_function='gaussian', sigma=1.5,
              learning_rate=0.5, random_seed=1)

# Inicializando os pesos e treinando o SOM, usando 5000 epocas
som.pca_weights_init(X)
som.train_random(X, 5000, verbose=True)

# Retorna o mapa de neurônios associado a cada paiz
country_map = som.labels_map(X, democracy_index.country)

# Plotando o mapa da democracia
plt.figure(figsize=(10, 10))
for p, countries in country_map.items():
    countries = list(countries)
    x = p[0] + .1
    y = p[1] - .3
    for i, c in enumerate(countries):
        off_set = (i+1)/len(countries) - 0.05
        plt.text(x, y+off_set, c, color=colors_dict[c], fontsize=8)
plt.pcolor(som.distance_map().T, cmap='gray_r', alpha=.8)
plt.xticks(np.arange(size+1))
plt.yticks(np.arange(size+1))
plt.grid()

legend_elements = [Patch(facecolor=clr,
                         edgecolor='w',
                         label=l) for l, clr in category_color.items()]
plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, .95))
plt.savefig('democracy.png')