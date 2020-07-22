

class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        super().__init__()

    def falar(self):
        print('{} disse oi!'.format(self.nome))
    
    def __str__(self):
        return self.nome


class Usuario(Pessoa):

    def __init__(self, nome, email, senha):
        self.email = email
        self.senha = senha
        super().__init__(nome)
    

p = Usuario('Leonardo', 'leonardo.santos@ifce.edu.br', 'senha')
p.falar()
print(p.email, p.senha)