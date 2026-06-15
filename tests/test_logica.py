from src.funcoes import (
    calcular_pontos,
    proxima_posicao,
    colidiu_com_parede,
    colidiu_com_corpo,
    direcao_valida,
    jogador_venceu,
    gerar_posicao_comida,
    limitar_valor,
)
from src.dados import atualizar_ranking


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_proxima_posicao():
    """Deve somar a direção à posição atual da cabeça."""
    assert proxima_posicao((5, 5), (0, 1)) == (5, 6)
    assert proxima_posicao((5, 5), (-1, 0)) == (4, 5)


def test_colidiu_com_parede():
    """Deve detectar posições fora dos limites da grade."""
    assert colidiu_com_parede((-1, 0), colunas=10, linhas=10) is True
    assert colidiu_com_parede((0, 10), colunas=10, linhas=10) is True
    assert colidiu_com_parede((5, 5), colunas=10, linhas=10) is False


def test_colidiu_com_corpo():
    """Deve detectar quando a posição coincide com algum segmento do corpo."""
    corpo = [(5, 5), (5, 4), (5, 3)]
    assert colidiu_com_corpo((5, 4), corpo) is True
    assert colidiu_com_corpo((5, 6), corpo) is False


def test_direcao_valida_impede_inversao():
    """Não deve permitir inverter o sentido diretamente."""
    assert direcao_valida((0, 1), (0, -1)) is False
    assert direcao_valida((0, 1), (-1, 0)) is True


def test_jogador_venceu():
    """Deve indicar vitória ao atingir ou superar a meta de pontos."""
    assert jogador_venceu(200, 200) is True
    assert jogador_venceu(210, 200) is True
    assert jogador_venceu(190, 200) is False


def test_gerar_posicao_comida_fora_do_corpo():
    """A comida sorteada nunca deve coincidir com o corpo da cobra."""
    corpo = [(linha, coluna) for linha in range(3) for coluna in range(3) if (linha, coluna) != (2, 2)]
    posicao = gerar_posicao_comida(corpo, colunas=3, linhas=3)
    assert posicao not in corpo


def test_atualizar_ranking_ordena_e_limita():
    """Deve manter o ranking ordenado do maior para o menor e respeitar o tamanho máximo."""
    ranking = [100, 80, 60]
    ranking = atualizar_ranking(ranking, 90, tamanho_maximo=3)
    assert ranking == [100, 90, 80]


def test_atualizar_ranking_vazio():
    """Deve funcionar corretamente com um ranking vazio."""
    ranking = atualizar_ranking([], 50, tamanho_maximo=5)
    assert ranking == [50]


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50
