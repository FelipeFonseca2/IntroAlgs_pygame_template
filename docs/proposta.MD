# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

> PySnake — Jogo da Cobrinha

## 2. Integrantes do grupo

- Felipe de Castro Fonseca
- João Pedro Fonseca Baiano

## 3. Tipo de jogo

> Jogo estilo Snake (cobrinha), com movimentação em grade, coleta de comida e crescimento progressivo da cobra.

## 4. Descrição geral do jogo

> Na tela aparece uma área de jogo em formato de grade com fundo xadrez, uma cobra com sprites visuais formada por vários segmentos e uma maçã posicionada aleatoriamente. A pontuação atual e o recorde são exibidos no título da janela.
>
> O jogador controla apenas a direção da cobra usando as setas do teclado; a cobra se movimenta sozinha, de forma contínua, na direção escolhida.
>
> O objetivo é guiar a cobra até a maçã para comê-la: cada maçã coletada aumenta a pontuação em 10 pontos e faz a cobra crescer um segmento. À medida que a cobra cresce, fica mais difícil se movimentar sem colidir.
>
> Os desafios principais são não bater nas paredes e não colidir com o próprio corpo, que vai ficando cada vez maior ao longo da partida.

## 5. Objetivo do jogador

> Obter a maior pontuação possível comendo o maior número de maçãs sem colidir com as paredes nem com o próprio corpo, tentando superar o recorde e atingir a meta de 2000 pontos para vencer.

## 6. Regras principais

- Regra 1: A cobra se movimenta de forma contínua e automática na direção atual; o jogador apenas altera a direção.
- Regra 2: Cada maçã coletada vale 10 pontos e faz a cobra crescer 1 segmento.
- Regra 3: A cobra não pode inverter o sentido diretamente (ex.: indo para a direita, não pode passar instantaneamente para a esquerda).
- Regra 4: Colidir com uma parede ou com o próprio corpo encerra a partida.
- Regra 5: Atingir 2000 pontos é a condição de vitória e exibe uma tela de parabéns.
- Regra 6: Ao fim de cada partida, a pontuação é adicionada ao ranking das 5 melhores e salva em arquivo.

## 7. Condição de vitória

> Atingir 2000 pontos. Ao alcançar essa meta, é exibida uma tela de vitória com a pontuação final e o ranking. O objetivo de longo prazo é sempre superar o recorde registrado.

## 8. Condição de derrota ou encerramento

> A partida termina quando a cobra colide com uma das paredes da área de jogo ou com o próprio corpo. É exibida uma tela de game over com a pontuação final e o ranking.

## 9. Elementos do jogo

### Jogador ou elemento principal

> A cobra, representada por uma lista de tuplas `(linha, coluna)`. Possui sprites distintos para cabeça (4 direções), corpo (reto e curvas) e cauda (4 direções). É controlada pelas setas do teclado e cresce a cada maçã coletada.

### Obstáculos, inimigos ou desafios

> As paredes da área de jogo e o próprio corpo da cobra, que aumenta a cada maçã e torna a movimentação progressivamente mais difícil.

### Itens, alvos ou objetos de interação

> A maçã, que aparece em uma posição aleatória livre da grade. Quando a cobra a alcança, a pontuação aumenta, a cobra cresce e uma nova maçã é gerada em outro lugar. Um som de coleta é reproduzido ao comer.

### Pontuação e ranking

> O jogo usa um sistema de pontuação (10 pontos por maçã) exibido no título da janela, um recorde individual e um ranking das 5 melhores pontuações, ambos salvos em arquivos de texto.

## 10. Controles

- Seta para cima: mover a cobra para cima
- Seta para baixo: mover a cobra para baixo
- Seta para esquerda: mover a cobra para a esquerda
- Seta para direita: mover a cobra para a direita
- Enter: reiniciar a partida (na tela de game over ou vitória)
- ESC: sair do jogo (na tela de game over ou vitória)

## 11. Organização do código

> - `main.py`: inicia o jogo;
> - `src/jogo.py`: loop principal, controle de estados (jogando, game over, vitória) e renderização com sprites;
> - `src/config.py`: configurações (tamanho da tela, grade, cores, velocidade, pontuação-alvo, caminhos de assets);
> - `src/funcoes.py`: funções de lógica (movimento, colisões, direção válida, geração de comida, pontuação);
> - `src/dados.py`: leitura e escrita do recorde e do ranking em arquivo;
> - `assets/imagens/`: sprites da cobra e da maçã (PNG);
> - `assets/fontes/`: fonte Kenney Pixel (TTF);
> - `assets/sons/`: efeito sonoro de coleta (OGG);
> - `tests/test_logica.py`: 12 testes das funções de lógica com pytest;
> - `docs/proposta.MD`: este documento;
> - `README.md`: documentação do projeto.

## 12. Recursos externos utilizados

> - Sprites da cobra e maçã: OpenGameArt.org (licença livre)
> - Fonte: Kenney Pixel (kenney.nl, licença CC0)
> - Som de coleta: EatSound por EugeneLoza (CC0)
> - Biblioteca: pygame-ce (fork do pygame com suporte a Python 3.14)

## 13. Estruturas de dados utilizadas

> - Lista de tuplas `(linha, coluna)` para o corpo da cobra
> - Tuplas para coordenadas e direções de movimento
> - Lista de inteiros para o ranking (top 5)
> - Dicionários para mapeamento de sprites por direção/estado

## 14. Uso de arquivos

> - `data/recorde.txt`: armazena o maior recorde em texto simples
> - `data/ranking.txt`: armazena as 5 melhores pontuações, uma por linha

## 15. Principais dificuldades encontradas

- Detecção de colisão com as paredes e com o próprio corpo da cobra.
- Controle da movimentação contínua, impedindo a inversão imediata de direção.
- Mapeamento correto dos sprites de curva do corpo da cobra para cada combinação de direções.
- Compatibilidade do pygame com Python 3.14 (resolvida com pygame-ce).

## 16. Escopo mínimo entregue

> Cobra controlada pelas setas, maçã aleatória que aumenta pontuação e tamanho, detecção de colisão com paredes e corpo, tela de game over e tela de vitória, ranking das 5 melhores pontuações salvo em arquivo, sprites visuais, fonte personalizada e efeito sonoro.

## 17. Possíveis melhorias futuras

- Tela inicial com menu e menu de pausa.
- Aumento progressivo da velocidade conforme a pontuação cresce.
- Obstáculos extras ou modo com bordas que teleportam a cobra para o lado oposto.
