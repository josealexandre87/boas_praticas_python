#models - É onde ficam estruturados os dados. (MVC)
class Pessoa:
    
    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    def nome_completo(self):
        #vai ter um erro de concatenação proposital
        #return self.nome + self.sobrenome
        return f'{self.nome} {self.sobrenome}'
