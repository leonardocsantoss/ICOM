# Lista

# Criando lista
l = [1, 2, 3, 4, "Leonardo", "ICOM"]
print(l)

# Adicionando no final da lista
l.append("ultimo")
print(l)

# Iniserindo no inicio da lista
l.insert(0, "primeiro")
print(l)

# Indice de um elemento
print(l.index("Leonardo"))

# Imprimindo um elemento pelo indice
print(l[0])

# Acesso
print(l[::2])


# Tupla
t = (1, 2, 3)
print(t)
print(len(t))


# Dicionario de dados
d = {
    'nome': 'Leonardo',
    'idade': 29,
    'data_de_nascimento': '12/...'
}
print(d)
print(d['nome'])
d['cansado'] = True

print(d)

print(d.get('data_de_hoje'))
