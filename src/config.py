# Configurações centrais do jogo (tela, cores, grade e caminhos de arquivos).
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60                  # taxa de renderização da tela
INTERVALO_COBRA = 100     # intervalo em ms entre cada movimento da cobra (100ms = 10 mov/s)

TITULO_JOGO = "PySnake"

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)
VERDE = (0, 200, 0)
VERDE_ESCURO = (0, 140, 0)
VERMELHO = (200, 0, 0)
AMARELO = (255, 220, 0)

# Cores do tabuleiro xadrez
VERDE_TABULEIRO_CLARO = (170, 215, 81)
VERDE_TABULEIRO_ESCURO = (157, 201, 69)

# Tamanho de cada célula da grade (em pixels) e dimensões da grade
TAMANHO_CELULA = 40
COLUNAS = LARGURA_TELA // TAMANHO_CELULA   # 20 colunas
LINHAS = ALTURA_TELA // TAMANHO_CELULA     # 15 linhas

# Pontuação necessária para vencer
PONTOS_VITORIA = 2000

# Quantidade máxima de entradas salvas no ranking
TAMANHO_RANKING = 5

CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.txt"

# Caminhos dos assets
CAMINHO_IMAGENS = "assets/imagens"
CAMINHO_FONTES = "assets/fontes"
CAMINHO_SONS = "assets/sons"
