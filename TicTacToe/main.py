import random
import gym
import gym_tictactoe


# Configurações
O = -1 # Usuário
X = 1 # IA
env = gym.make("TicTacToe-v1", symbols=[X, O])
env.reset()


def action_O(last_state):
    '''
        Gera a ação do usuário.
        last_state = lista de ações realizadas
    '''
    options = [i for i in range(len(last_state)) if last_state[i] == 0]
    print('Options: %s' % options)
    action = int(input('Select a option: '))
    while not action in options:
        action = int(input('Select a option: '))
    return action

def action_X(last_state):
    '''
        Gera a ação da IA.
        Inicialmente é aleatória
        last_state = lista de ações realizadas
    '''
    options = [i for i in range(len(last_state)) if last_state[i] == 0]
    return random.choice(options)


# Define o usuário da vez
user = O
# Ultimo estado
last_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Inicia o jogo
env.render(mode=None)
while True:
    # Cada usuário tem estratégias diferentes
    if user == O:
        action = action_O(last_state)
    else:
        action = action_X(last_state)

    print('Play: %s Action: %s' % ('O' if user == O else 'X', action))
    state, reward, done, infos = env.step(action, user)
    print(state, reward, done, infos)
    env.render(mode=None)

    # Se terminou mostra o placar
    if done:
        if reward == 10:
            print("Draw !")
        else:
            print("User %s wins! Reward : %s" % ('O' if user == O else 'X', reward, ))
        env.reset()
        break
    # Muda o usuário
    user = O if user == X else X
    last_state = state
env.close()

