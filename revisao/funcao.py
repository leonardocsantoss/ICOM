
def soma(n1, n2=5):
    return n1+n2


s = soma(2)
print(s)

def imprimir(nome, idade):
    print('Nome: ', nome)
    print('Idade: ', idade)


imprimir(idade=29, nome='Leonardo')


def imprimi2(*args, **kargs):
    print(args)
    print(kargs)


imprimi2('leonardo', 'ICOM', 1, 2, 3, nome='leonardo', idade=29)





'''
Uma clínica lhe contratou para desenvolver um sistema que gerencia a lista de clientes a ser atendidos.
Cada cliente possuí nome, sexo e o tipo de atendimento(normal ou preferencial).
Os clientes são atendidos de acordo com a ordem e chegada, sendo os preferenciais antedidos antes dos normais.
O sistema deve:
1. Adicionar Cliente
2. Atender Cliente
3. Consultar próximo Cliente

Obs.: Utilize funções.
'''


clientes = []

def criarCliente(nome, sexo, atendimento):
    return {
        'nome': nome,
        'sexo': sexo, 
        'atendimento': atendimento
    }

def adicionarCliente():
    nome = input('Digite o seu nome: ')
    sexo = input('Informe o seu sexo(m/f): ')
    atendimento = input('Tipo de atendimento (p-Preferencial e n-Normal): ')

    c = criarCliente(nome, sexo, atendimento)
    if atendimento == 'n':
        clientes.append(c)
    else:
        clientes.insert(0, c)

def atenderCliente():
    c = clientes.pop(0)
    print('Cliente atendido: ', c['nome'])

def consultarCliente():
    print('Próximo Cliente da fila: ', clientes[0]['nome'])

while True:
    op = int(input('1. Adicionar Cliente\n2. Atender Cliente\n3. Consultar próximo Cliente\n Opção: '))
    if op == 1:
        adicionarCliente()
    elif op == 2:
        atenderCliente()
    elif op == 3:
        consultarCliente()