'''
Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não.
Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 
- Ter no mínimo 65 anos de idade. 
- Ter trabalhado no mínimo 30 anos. 
- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 
Com base nas informações acima, faça um algoritmo que leia:
    o número do empregado (código), o ano de seu nascimento, o ano de seu ingresso na empresa e o ano que estamos.
    O programa deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.

'''

codigo = input("Digite o seu código: ")
ano_nasc = int(input("Digite o ano do seu nascimento: "))
ano_ingresso = int(input("Digite o ano de ingresso na empresa: "))
ano = int(input("Digite o ano que estamos: "))

idade = ano - ano_nasc
tempo = ano - ano_ingresso

if idade >= 65:
    print('Requerer aposentadoria')
elif tempo >= 30:
    print('Requerer aposentadoria')
elif idade >= 60 and tempo >= 25:
    print('Requerer aposentadoria')
else:
    print('Não requerer')

