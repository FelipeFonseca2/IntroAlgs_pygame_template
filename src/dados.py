def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo == "":
                return 0
            return int(conteudo)
    except FileNotFoundError:
        return 0


def salvar_ranking(caminho_arquivo, ranking):
    """Salva a lista de pontuações do ranking em arquivo, uma por linha."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for pontuacao in ranking:
            arquivo.write(str(pontuacao) + "\n")


def carregar_ranking(caminho_arquivo):
    """Carrega o ranking do arquivo; retorna lista vazia se não existir."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.read().strip().splitlines()
            return [int(linha) for linha in linhas if linha.strip().isdigit()]
    except FileNotFoundError:
        return []


def atualizar_ranking(ranking, pontuacao, tamanho_maximo):
    """Insere a pontuação no ranking, mantém ordenado e limita o tamanho."""
    ranking.append(pontuacao)
    ranking.sort(reverse=True)
    return ranking[:tamanho_maximo]
