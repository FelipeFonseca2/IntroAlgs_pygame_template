import pygame
import os

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    VERDE_TABULEIRO_CLARO,
    VERDE_TABULEIRO_ESCURO,
    VERMELHO,
    AMARELO,
    PRETO,
    BRANCO,
    CINZA,
    TAMANHO_CELULA,
    COLUNAS,
    LINHAS,
    PONTOS_VITORIA,
    TAMANHO_RANKING,
    CAMINHO_RECORDE,
    CAMINHO_RANKING,
    CAMINHO_IMAGENS,
    CAMINHO_FONTES,
    CAMINHO_SONS,
    INTERVALO_COBRA,
)

from src.funcoes import (
    calcular_pontos,
    proxima_posicao,
    colidiu_com_parede,
    colidiu_com_corpo,
    direcao_valida,
    jogador_venceu,
    gerar_posicao_comida,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking,
    atualizar_ranking,
)

# Direções representadas como (delta_linha, delta_coluna)
CIMA     = (-1,  0)
BAIXO    = ( 1,  0)
ESQUERDA = ( 0, -1)
DIREITA  = ( 0,  1)

# Estados do jogo
JOGANDO   = "jogando"
GAME_OVER = "game_over"
VITORIA   = "vitoria"

# Mapeia (dir_para_cabeça, dir_para_cauda) → nome do sprite de corpo
# Cada sprite conecta os dois lados nomeados:
#   topleft    = conecta borda SUPERIOR e borda ESQUERDA
#   topright   = conecta borda SUPERIOR e borda DIREITA
#   bottomleft = conecta borda INFERIOR e borda ESQUERDA
#   bottomright= conecta borda INFERIOR e borda DIREITA
MAPA_CORPO = {
    # reto
    (( 0, -1), ( 0,  1)): "body_horizontal",
    (( 0,  1), ( 0, -1)): "body_horizontal",
    ((-1,  0), ( 1,  0)): "body_vertical",
    (( 1,  0), (-1,  0)): "body_vertical",
    # curvas
    ((-1,  0), ( 0, -1)): "body_topleft",
    (( 0,  1), (-1,  0)): "body_topright",
    ((-1,  0), ( 0,  1)): "body_topright",
    (( 0, -1), (-1,  0)): "body_topleft",
    (( 1,  0), ( 0, -1)): "body_bottomleft",
    (( 0,  1), ( 1,  0)): "body_bottomright",
    (( 1,  0), ( 0,  1)): "body_bottomright",
    (( 0, -1), ( 1,  0)): "body_bottomleft",
}

# Mapeia direção_de_movimento → nome do sprite de cabeça
MAPA_CABECA = {
    CIMA:     "head_up",
    BAIXO:    "head_down",
    ESQUERDA: "head_left",
    DIREITA:  "head_right",
}

# Mapeia direção_da_cauda_para_o_corpo → nome do sprite de cauda
MAPA_CAUDA = {
    DIREITA:  "tail_right",
    ESQUERDA: "tail_left",
    BAIXO:    "tail_down",
    CIMA:     "tail_up",
}


def carregar_sprites():
    """Carrega e escala todos os sprites do jogo a partir da pasta de imagens."""
    def img(nome):
        caminho = os.path.join(CAMINHO_IMAGENS, nome)
        return pygame.transform.scale(
            pygame.image.load(caminho).convert_alpha(),
            (TAMANHO_CELULA, TAMANHO_CELULA),
        )

    nomes = [
        "apple",
        "head_up", "head_down", "head_left", "head_right",
        "body_horizontal", "body_vertical",
        "body_topleft", "body_topright", "body_bottomleft", "body_bottomright",
        "tail_up", "tail_down", "tail_left", "tail_right",
    ]
    return {nome: img(f"{nome}.png") for nome in nomes}


def carregar_sons():
    """Carrega os efeitos sonoros do jogo."""
    som_comer = pygame.mixer.Sound(os.path.join(CAMINHO_SONS, "EatSound_CC0_by_EugeneLoza.ogg"))
    return som_comer


def desenhar_tabuleiro(tela):
    """Desenha o fundo xadrez com duas tonalidades de verde."""
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            cor = VERDE_TABULEIRO_CLARO if (linha + coluna) % 2 == 0 else VERDE_TABULEIRO_ESCURO
            rect = pygame.Rect(coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            pygame.draw.rect(tela, cor, rect)


def desenhar_cobra(tela, sprites, cobra, direcao):
    """Desenha a cobra segmento a segmento usando os sprites corretos."""
    for i, segmento in enumerate(cobra):
        linha, coluna = segmento
        x = coluna * TAMANHO_CELULA
        y = linha * TAMANHO_CELULA

        if i == 0:
            # Cabeça: usa a direção atual do movimento
            sprite = sprites[MAPA_CABECA[direcao]]

        elif i == len(cobra) - 1:
            # Cauda: aponta para FORA do corpo (oposto ao segmento anterior)
            anterior = cobra[i - 1]
            dir_cauda = (segmento[0] - anterior[0], segmento[1] - anterior[1])
            sprite = sprites[MAPA_CAUDA.get(dir_cauda, "tail_right")]

        else:
            # Corpo: determina sprite com base nos segmentos vizinhos
            anterior = cobra[i - 1]
            proximo  = cobra[i + 1]
            dir_ant  = (anterior[0] - segmento[0], anterior[1] - segmento[1])
            dir_prox = (proximo[0]  - segmento[0], proximo[1]  - segmento[1])
            nome = MAPA_CORPO.get((dir_ant, dir_prox), "body_horizontal")
            sprite = sprites[nome]

        tela.blit(sprite, (x, y))


def desenhar_texto(tela, fonte, texto, tamanho, cor, x, y, centralizado=True):
    """Renderiza texto na tela na posição indicada."""
    f = fonte if fonte else pygame.font.SysFont(None, tamanho)
    superficie = f.render(texto, True, cor)
    retangulo = superficie.get_rect()
    if centralizado:
        retangulo.center = (x, y)
    else:
        retangulo.topleft = (x, y)
    tela.blit(superficie, retangulo)


def desenhar_tela_final(tela, fonte, estado, pontos, recorde, ranking):
    """Desenha a tela de game over ou vitória com pontuação e ranking."""
    tela.fill(PRETO)

    titulo = "VOCE VENCEU!" if estado == VITORIA else "GAME OVER"
    cor_titulo = AMARELO if estado == VITORIA else VERMELHO
    desenhar_texto(tela, fonte, titulo, 80, cor_titulo, LARGURA_TELA // 2, 100)
    desenhar_texto(tela, fonte, f"Pontuacao: {pontos}", 50, BRANCO, LARGURA_TELA // 2, 190)
    desenhar_texto(tela, fonte, f"Recorde:   {recorde}", 36, CINZA,  LARGURA_TELA // 2, 245)
    desenhar_texto(tela, fonte, "TOP 5", 40, AMARELO, LARGURA_TELA // 2, 310)
    for i, p in enumerate(ranking):
        desenhar_texto(tela, fonte, f"{i + 1}.  {p}", 32, BRANCO, LARGURA_TELA // 2, 350 + i * 36)
    desenhar_texto(tela, fonte, "Enter: jogar novamente    ESC: sair", 26, CINZA, LARGURA_TELA // 2, ALTURA_TELA - 40)


def criar_cobra():
    """Cria a cobra inicial com 3 segmentos no centro da grade."""
    centro = (LINHAS // 2, COLUNAS // 2)
    return [centro, (centro[0], centro[1] - 1), (centro[0], centro[1] - 2)]


def executar_jogo():
    """Executa o loop principal do jogo: movimenta a cobra, trata colisões e pontuação."""
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    sprites = carregar_sprites()
    som_comer = carregar_sons()

    caminho_fonte = os.path.join(CAMINHO_FONTES, "Kenney Pixel.ttf")
    fonte_grande = pygame.font.Font(caminho_fonte, 72)
    fonte_media  = pygame.font.Font(caminho_fonte, 40)
    fonte_pequena = pygame.font.Font(caminho_fonte, 28)

    recorde = carregar_recorde(CAMINHO_RECORDE)
    ranking = carregar_ranking(CAMINHO_RANKING)

    cobra   = criar_cobra()
    direcao = DIREITA
    comida  = gerar_posicao_comida(cobra, COLUNAS, LINHAS)
    pontos  = 0
    estado  = JOGANDO

    # Timer independente para mover a cobra sem travar a renderização
    MOVER_COBRA = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVER_COBRA, INTERVALO_COBRA)

    rodando = True
    while rodando:
        relogio.tick(FPS)

        mover = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == MOVER_COBRA:
                mover = True

            elif evento.type == pygame.KEYDOWN:
                if estado == JOGANDO:
                    if evento.key == pygame.K_UP and direcao_valida(direcao, CIMA):
                        direcao = CIMA
                    elif evento.key == pygame.K_DOWN and direcao_valida(direcao, BAIXO):
                        direcao = BAIXO
                    elif evento.key == pygame.K_LEFT and direcao_valida(direcao, ESQUERDA):
                        direcao = ESQUERDA
                    elif evento.key == pygame.K_RIGHT and direcao_valida(direcao, DIREITA):
                        direcao = DIREITA

                elif estado in (GAME_OVER, VITORIA):
                    if evento.key == pygame.K_RETURN:
                        cobra   = criar_cobra()
                        direcao = DIREITA
                        comida  = gerar_posicao_comida(cobra, COLUNAS, LINHAS)
                        pontos  = 0
                        estado  = JOGANDO
                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

        if estado == JOGANDO and mover:
            nova_cabeca = proxima_posicao(cobra[0], direcao)

            if colidiu_com_parede(nova_cabeca, COLUNAS, LINHAS) or colidiu_com_corpo(nova_cabeca, cobra):
                estado  = GAME_OVER
                ranking = atualizar_ranking(ranking, pontos, TAMANHO_RANKING)
                salvar_ranking(CAMINHO_RANKING, ranking)
                if pontos > recorde:
                    recorde = pontos
                    salvar_recorde(CAMINHO_RECORDE, recorde)
            else:
                cobra.insert(0, nova_cabeca)

                if nova_cabeca == comida:
                    som_comer.play()
                    pontos = calcular_pontos(pontos, 10)
                    comida = gerar_posicao_comida(cobra, COLUNAS, LINHAS)

                    if pontos > recorde:
                        recorde = pontos
                        salvar_recorde(CAMINHO_RECORDE, recorde)

                    if jogador_venceu(pontos, PONTOS_VITORIA):
                        estado  = VITORIA
                        ranking = atualizar_ranking(ranking, pontos, TAMANHO_RANKING)
                        salvar_ranking(CAMINHO_RANKING, ranking)
                else:
                    cobra.pop()

            pygame.display.set_caption(
                f"{TITULO_JOGO}  |  Pontos: {pontos}  |  Recorde: {recorde}  |  Meta: {PONTOS_VITORIA}"
            )

        # Renderização
        if estado == JOGANDO:
            desenhar_tabuleiro(tela)
            tela.blit(sprites["apple"], (comida[1] * TAMANHO_CELULA, comida[0] * TAMANHO_CELULA))
            desenhar_cobra(tela, sprites, cobra, direcao)
        else:
            desenhar_tela_final(tela, fonte_media, estado, pontos, recorde, ranking)

        pygame.display.flip()

    pygame.quit()
