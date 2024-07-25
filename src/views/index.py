#views - é onde temos as interações com o usuário - interface grafica ou não (MVC)
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#print(f"Root path: {root}")
#print(f"sys.path: {sys.path}")

from controller.pessoa import PessoaController
from models.pessoa import Pessoa

#Agora podemos interagir com o usuário usando a controller e os models

while True:
    decisao = int(input("Digite 1 para salvar os dados e 2 para  listar: "))
    if decisao == 1:
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")

        dados_pessoa = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
        PessoaController.salvar_pessoa(dados_pessoa)

    elif decisao == 2:
        for pessoa in PessoaController.listar_pessoas():
            print(f"Nome: {pessoa.nome}")




