# PySnake

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Felipe de Castro Fonseca
- João Pedro Fonseca Baiano

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> O jogo é uma versão do clássico Snake. O jogador controla uma cobra que se movimenta continuamente pela tela e deve guiá-la até a comida. Cada comida coletada aumenta a pontuação e faz a cobra crescer um segmento, tornando a movimentação progressivamente mais difícil. O desafio é não colidir com as paredes nem com o próprio corpo.

## Objetivo do jogador

> Obter a maior pontuação possível comendo o maior número de comidas sem colidir com as paredes nem com o próprio corpo, tentando superar o recorde e atingir a meta de 2000 pontos para vencer.

## Regras do jogo

- A cobra se movimenta de forma contínua e automática na direção atual; o jogador apenas altera a direção.
- Cada comida coletada vale 10 pontos e faz a cobra crescer 1 segmento.
- A cobra não pode inverter o sentido diretamente (ex.: indo para a direita, não pode ir instantaneamente para a esquerda).
- Colidir com uma parede ou com o próprio corpo encerra a partida.
- Atingir 2000 pontos é a condição de vitória.
- Ao fim de cada partida, a pontuação é adicionada ao ranking das 5 melhores e salva em arquivo.

## Controles

- Seta para cima: mover a cobra para cima
- Seta para baixo: mover a cobra para baixo
- Seta para esquerda: mover a cobra para a esquerda
- Seta para direita: mover a cobra para a direita
- Enter: reiniciar a partida (na tela de game over ou vitória)
- ESC: sair do jogo (na tela de game over ou vitória)

## Como executar o projeto

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```
