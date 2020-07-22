'''
    Calcule a média de uma série de valores digitados pelo usuário, a série será interrompida quando o usuário digitar o número 0.
'''

soma = 0
cont = 0

num = int(input("Digite um número: "))
while num != 0:
    soma += num
    cont += 1
    num = int(input("Digite um número: "))


print("Media: ", soma/cont)