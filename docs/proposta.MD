# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

> PySnake — Jogo da Cobrinha

## 2. Integrantes do grupo

- Nome 1: Felipe de Castro Fonseca

## 3. Tipo de jogo

> Jogo estilo Snake (cobrinha), com movimentação em grade, coleta de comida e crescimento progressivo da cobra.

## 4. Descrição geral do jogo

> Na tela aparece uma área de jogo em formato de grade, uma cobra formada por vários segmentos e uma comida posicionada aleatoriamente. No topo da tela (e/ou no título da janela) são exibidos a pontuação atual e o recorde.
>
> O jogador controla apenas a direção da cobra usando as setas do teclado; a cobra se movimenta sozinha, de forma contínua, na direção escolhida.
>
> O objetivo é guiar a cobra até a comida para comê-la: cada comida aumenta a pontuação e faz a cobra crescer um segmento. À medida que a cobra cresce, fica mais difícil se movimentar sem colidir.
>
> Os desafios principais são não bater nas paredes e não colidir com o próprio corpo, que vai ficando cada vez maior ao longo da partida.

## 5. Objetivo do jogador

> Obter a maior pontuação possível, comendo o maior número de comidas sem colidir com as paredes nem com o próprio corpo, tentando superar o recorde salvo no ranking.

## 6. Regras principais

- Regra 1: A cobra se movimenta de forma contínua e automática na direção atual; o jogador apenas altera a direção.
- Regra 2: Cada comida coletada vale 10 pontos e faz a cobra crescer 1 segmento.
- Regra 3: A cobra não pode inverter o sentido diretamente (ex.: indo para a direita, não pode passar instantaneamente para a esquerda).
- Regra 4: Colidir com uma parede ou com o próprio corpo encerra a partida.
- Regra 5: Ao fim da partida, a pontuação é comparada ao ranking e, se for uma das melhores, é salva em arquivo.

## 7. Condição de vitória

> Como o Snake é um jogo de pontuação contínua, definimos a "vitória" como atingir uma pontuação-alvo configurável (por exemplo, 200 pontos), que exibe uma tela de parabéns. O objetivo de longo prazo é sempre superar o recorde registrado no ranking.

## 8. Condição de derrota ou encerramento

> A partida termina quando a cobra colide com uma das paredes da área de jogo ou com o próprio corpo. Nesse momento é exibida a tela de fim de jogo com a pontuação final.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

> A cobra, representada por uma lista de coordenadas (cada segmento é uma posição na grade). É controlada pelas setas do teclado e cresce a cada comida coletada.

## Obstáculos, inimigos ou desafios

> As paredes da área de jogo e o próprio corpo da cobra, que aumenta a cada comida e torna a movimentação progressivamente mais difícil.

## Itens, alvos ou objetos de interação

> A comida (uma maçã), que aparece em uma posição aleatória livre da grade. Quando a cobra a alcança, a comida some, a pontuação aumenta, a cobra cresce e uma nova comida é gerada em outro lugar.

## Pontuação, vidas, tempo ou progresso

> O jogo usa um sistema de pontuação (10 pontos por comida) exibido na tela, e um ranking/recorde salvo em arquivo. As estruturas de dados previstas são: uma lista de tuplas para o corpo da cobra, tuplas para as coordenadas (linha, coluna), um dicionário para as configurações do jogo e uma lista de dicionários para o ranking (nome e pontuação).

## 10. Controles previstos

- Seta para cima: mover a cobra para cima
- Seta para baixo: mover a cobra para baixo
- Seta para esquerda: mover a cobra para a esquerda
- Seta para direita: mover a cobra para a direita
- Enter / Espaço: iniciar ou reiniciar a partida
- ESC: sair do jogo

## 11. Organização inicial do código

> - `main.py`: inicia o jogo;
> - `src/jogo.py`: contém o loop principal e o controle de estados (jogando, fim de jogo);
> - `src/config.py`: guarda configurações como tamanho da tela, tamanho da grade, cores, velocidade e pontuação-alvo;
> - `src/funcoes.py`: funções auxiliares (mover a cobra, detectar colisões, gerar comida, calcular pontuação, desenhar os elementos);
> - `src/dados.py`: funções de leitura e escrita do ranking/recorde em arquivo;
> - `tests/test_funcoes.py`: testes simples das funções de lógica (colisão, crescimento, pontuação, geração de comida);
> - `docs/proposta.md`: este documento;
> - `README.md`: documentação básica do projeto.

## 12. Recursos externos previstos

> Pretendemos manter o jogo simples, usando principalmente formas geométricas desenhadas pelo próprio Pygame. Caso haja tempo, poderemos incluir alguns sons gratuitos (ex.: efeito ao comer) e uma fonte personalizada gratuita. Tutoriais poderão ser usados apenas como referência. O ranking será gravado em um arquivo (texto ou JSON) dentro do próprio projeto.

## 13. Principais dificuldades esperadas

- Dificuldade 1: Detecção de colisão (com as paredes e com o próprio corpo da cobra).
- Dificuldade 2: Controle da movimentação contínua, impedindo a inversão imediata de direção.
- Dificuldade 3: Leitura e escrita do ranking em arquivo, além da organização modular do código e do uso do GitHub.

## 14. Escopo mínimo para a entrega final

> A versão mínima terá: uma cobra controlada pelas setas, comida que aparece aleatoriamente e aumenta a pontuação e o tamanho da cobra, detecção de colisão com as paredes e com o próprio corpo, exibição da pontuação na tela, tela de fim de jogo e ranking salvo em arquivo. O código será organizado em funções e módulos, com testes simples para as funções de lógica.

## 15. Possíveis melhorias, caso haja tempo

- Melhoria 1: Tela inicial / menu e menu de pausa.
- Melhoria 2: Aumento progressivo da velocidade conforme a pontuação cresce.
- Melhoria 3: Sons, efeitos visuais e obstáculos extras (ou modo com bordas que teleportam a cobra para o lado oposto).