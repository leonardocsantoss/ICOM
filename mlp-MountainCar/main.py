import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

env = gym.make("MountainCar-v0")
env.reset()


def model_data_preparation(tests_count=10000):
    def goal(obs, prev_obs):
        # Métrica usada é o aumento de velocidade
        if abs(obs[1]) > abs(prev_obs[1]):
            return True
        return False

    print('Init model_data_preparation...')
    training_data = []
    prev_obs = env.reset()
    for game_index in range(tests_count):
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        if goal(obs, prev_obs):
            # Usa a posição do 1 como acão
            if action == 0:
                output = [1, 0, 0]
            elif action == 1:
                output = [0, 1, 0]
            elif action == 2:
                output = [0, 0, 1]
            training_data.append([prev_obs, output])
        prev_obs = obs
        if done:
            prev_obs = env.reset()
    print('len(training_data) = ', len(training_data))
    return training_data


def build_model(input_size, output_size):
    print('Init build_model...')
    model = Sequential()
    model.add(Dense(128, input_dim=input_size, activation='relu'))
    model.add(Dense(52, activation='relu'))
    model.add(Dense(output_size, activation='linear'))
    model.compile(loss='mse', optimizer=Adam())
    return model


def train_model(training_data):
    print('Init train_model...')
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]))
    y = np.array([i[1] for i in training_data]).reshape(-1, len(training_data[0][1]))
    model = build_model(input_size=len(X[0]), output_size=len(y[0]))
    model.fit(X, y, epochs=10)
    return model


training_data = model_data_preparation()
trained_model = train_model(training_data)


print('Init play game')
# 100 jogos
for each_game in range(100):
    prev_obs = env.reset()
    # 500 passos cada jogo
    for step_index in range(500):
        env.render()
        print(prev_obs, type(prev_obs), prev_obs.reshape(-1, len(prev_obs)))
        action = np.argmax(trained_model.predict(prev_obs.reshape(-1, len(prev_obs)))[0])
        obs, reward, done, info = env.step(action)
        prev_obs = obs
        if done:
            break