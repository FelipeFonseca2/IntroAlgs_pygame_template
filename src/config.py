# Configurações centrais do jogo (tela, cores, grade e caminhos de arquivos).
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 10  # velocidade da cobra (atualizações por segundo)

TITULO_JOGO = "PySnake"

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)

# Tamanho de cada célula da grade (em pixels) e dimensões da grade
TAMANHO_CELULA = 20
COLUNAS = LARGURA_TELA // TAMANHO_CELULA
LINHAS = ALTURA_TELA // TAMANHO_CELULA

CAMINHO_RECORDE = "data/recorde.txt"
