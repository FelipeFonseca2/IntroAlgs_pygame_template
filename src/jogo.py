import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    VERDE,
    VERMELHO,
    PRETO,
    TAMANHO_CELULA,
    COLUNAS,
    LINHAS,
    CAMINHO_RECORDE,
)

from src.funcoes import (
    calcular_pontos,
    proxima_posicao,
    colidiu_com_parede,
    colidiu_com_corpo,
    direcao_valida,
    gerar_posicao_comida,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

# Direções representadas como (delta_linha, delta_coluna)
CIMA = (-1, 0)
BAIXO = (1, 0)
ESQUERDA = (0, -1)
DIREITA = (0, 1)


def desenhar_celula(tela, posicao, cor):
    """Desenha um quadrado na grade a partir de uma posição (linha, coluna)."""
    linha, coluna = posicao
    retangulo = pygame.Rect(
        coluna * TAMANHO_CELULA,
        linha * TAMANHO_CELULA,
        TAMANHO_CELULA,
        TAMANHO_CELULA,
    )
    pygame.draw.rect(tela, cor, retangulo)


def executar_jogo():
    """Executa o loop principal do jogo: movimenta a cobra, trata colisões e pontuação."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    # Estado inicial: cobra com 3 segmentos no centro da grade, andando para a direita
    centro = (LINHAS // 2, COLUNAS // 2)
    cobra = [centro, (centro[0], centro[1] - 1), (centro[0], centro[1] - 2)]
    direcao = DIREITA

    comida = gerar_posicao_comida(cobra, COLUNAS, LINHAS)

    pontos = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao_valida(direcao, CIMA):
                    direcao = CIMA
                elif evento.key == pygame.K_DOWN and direcao_valida(direcao, BAIXO):
                    direcao = BAIXO
                elif evento.key == pygame.K_LEFT and direcao_valida(direcao, ESQUERDA):
                    direcao = ESQUERDA
                elif evento.key == pygame.K_RIGHT and direcao_valida(direcao, DIREITA):
                    direcao = DIREITA

        # Calcula a nova posição da cabeça da cobra
        nova_cabeca = proxima_posicao(cobra[0], direcao)

        # Verifica colisão com paredes ou com o próprio corpo: encerra a partida
        if colidiu_com_parede(nova_cabeca, COLUNAS, LINHAS) or colidiu_com_corpo(nova_cabeca, cobra):
            rodando = False
            continue

        cobra.insert(0, nova_cabeca)

        # Verifica se a cobra alcançou a comida
        if nova_cabeca == comida:
            pontos = calcular_pontos(pontos, 10)
            comida = gerar_posicao_comida(cobra, COLUNAS, LINHAS)
        else:
            # Sem comer, a cauda anda junto (remove o último segmento)
            cobra.pop()

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde}"
        )

        tela.fill(PRETO)

        # Desenha a comida e cada segmento da cobra como quadrados na grade
        desenhar_celula(tela, comida, VERMELHO)
        for segmento in cobra:
            desenhar_celula(tela, segmento, VERDE)

        pygame.display.flip()

    pygame.quit()
