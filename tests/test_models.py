import sys
sys.path.append(".")
from src.models import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Jonas', 'Almeida', 23, 1233443332)
    assert p1.nome_completo() == 'Jonas Almeida'