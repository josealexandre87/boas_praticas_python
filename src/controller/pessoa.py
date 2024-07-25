#controllers - É onde contém a lógica dos dados em models. (MVC)
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.pessoa import Pessoa
from typing import List

class PessoaController:
    pessoa = []
    # pessoa: Pessoa: Um parâmetro adicional que é esperado pelo método.
    @classmethod
    def salvar_pessoa(cls, pessoa: Pessoa) -> None:
        cls.pessoa.append(pessoa) # Adiciona instâncias tipo Pessoa na lista.
    
    @classmethod
    def listar_pessoas(cls) -> List[Pessoa]:
        return cls.pessoa

"""
@classmethod
O decorador @classmethod é utilizado para definir métodos que estão vinculados à classe e não à instância da classe. Um método de classe recebe a própria classe como o primeiro argumento, geralmente denominado cls, ao invés da instância (que é passada para métodos de instância como self).

cls
cls é uma convenção para representar a própria classe dentro de um método de classe, semelhante a como self é usado para representar a instância dentro de um método de instância. Você pode usar cls para acessar atributos e métodos de classe."""