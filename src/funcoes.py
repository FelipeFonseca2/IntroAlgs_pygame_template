import random


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def proxima_posicao(cabeca, direcao):
    """Calcula a próxima posição (linha, coluna) da cabeça da cobra."""
    linha, coluna = cabeca
    delta_linha, delta_coluna = direcao
    return (linha + delta_linha, coluna + delta_coluna)


def colidiu_com_parede(posicao, colunas, linhas):
    """Verifica se a posição está fora dos limites da grade."""
    linha, coluna = posicao
    return coluna < 0 or coluna >= colunas or linha < 0 or linha >= linhas


def colidiu_com_corpo(posicao, corpo):
    """Verifica se a posição colide com algum segmento do corpo da cobra."""
    return posicao in corpo


def direcao_valida(direcao_atual, nova_direcao):
    """Impede que a cobra inverta o sentido diretamente (ex.: direita -> esquerda)."""
    linha_atual, coluna_atual = direcao_atual
    nova_linha, nova_coluna = nova_direcao
    return (linha_atual, coluna_atual) != (-nova_linha, -nova_coluna)


def jogador_venceu(pontos, meta):
    """Verifica se o jogador atingiu a pontuação necessária para vencer."""
    return pontos >= meta


def gerar_posicao_comida(corpo, colunas, linhas):
    """Sorteia uma posição livre da grade para a comida."""
    while True:
        posicao = (random.randint(0, linhas - 1), random.randint(0, colunas - 1))
        if posicao not in corpo:
            return posicao


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor
