import numpy as np

# Mapa 5x5
mapa = np.random.randint(1, 10, size=(5, 5))

# Posiciona o tesouro em uma posição aleatória
while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0


def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1

    mapa_com_jogador_str = np.char.mod(
        '%2d', mapa_com_jogador)  # Converte a matriz para string
    mapa_com_jogador_str[mapa_com_jogador == '-1'] = 'P'

    print("\nMapa Atual:")
    for linha in mapa_com_jogador_str:
        print(" ".join(linha))


# Fluxo principal
while True:
    mostrar_mapa(mapa, posicao_jogador)

    direcao = input(
        "Informe a direcao que deseja mover: (cima, baixo, esquerda, direita)").strip().lower()

    movimentos = {
        "cima": (-1, 0),
        "baixo": (1, 0),
        "esquerda": (0, -1),
        "direita": (0, 1),
        "c": (-1, 0),
        "b": (1, 0),
        "e": (0, -1),
        "d": (0, 1)
    }

    if direcao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcao]
                        [0], posicao_jogador[1]+movimentos[direcao][1])
    else:
        print("Direção invalida! Tente novamente.")

    # Verifica se a nova posicao é válida
    if not (0 <= nova_posicao[0] < mapa.shape[0] and 0 <= nova_posicao[1] < mapa.shape[1]):
        print("Movimento fora dos limites! Tente novamente.")
        continue

    posicao_jogador = nova_posicao
    pontuacao += 1

    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print("\n\n=====Parabéns!! Você encontro o tesouro!=====")
        print(f"Pontuação final: {pontuacao}")
        print(
            f"O Tesouro estava na posicao: ({tesouro_linha, tesouro_coluna})")
