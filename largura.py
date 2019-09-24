from copy import deepcopy


# Numero de rainhas que devem ser colocadas no tabuleiro
numero_rainhas = 8


class Estado:
    def __init__(self, tabuleiro, rainhas, colunas, linhas, diagonais_principais, diagonais_secundarias):
        self.tabuleiro = tabuleiro
        self.rainhas = rainhas
        self.colunas = colunas
        self.linhas = linhas
        self.diagonais_principais = diagonais_principais
        self.diagonais_secundarias = diagonais_secundarias


def gerar_filhos(estado):
    abertos = []

    for coluna in range(numero_rainhas):
        for linha in range(numero_rainhas):
            if ((estado.diagonais_principais[linha - coluna + numero_rainhas - 1] != 1 and
                 estado.diagonais_secundarias[linha + coluna] != 1) and
                    estado.colunas[coluna] != 1 and estado.linhas[linha] != 1):

                estado_atual = deepcopy(estado)

                estado_atual.tabuleiro[linha][coluna] = 1
                estado_atual.rainhas = estado_atual.rainhas + 1
                estado_atual.colunas[coluna] = 1
                estado_atual.linhas[linha] = 1
                estado_atual.diagonais_principais[linha - coluna + numero_rainhas - 1] = 1
                estado_atual.diagonais_secundarias[linha + coluna] = 1

                abertos.append(estado_atual)
                break

    return abertos


def largura(estado_inicial):
    abertos = [estado_inicial]

    while len(abertos) != 0:
        estado = abertos[0]

        if estado.rainhas == numero_rainhas:
            return estado

        abertos = abertos + gerar_filhos(estado)
        abertos.pop(0)

    return None


def encontrar_solucao():
    tabuleiro = [[0 for linha in range(numero_rainhas)] for coluna in range(numero_rainhas)]
    rainhas = 0
    colunas = [0] * numero_rainhas
    linhas = [0] * numero_rainhas
    diagonais_principais = [0] * (numero_rainhas * 2 - 1)
    diagonais_secundarias = [0] * (numero_rainhas * 2)

    estado_inicial = Estado(tabuleiro, rainhas, colunas, linhas, diagonais_principais, diagonais_secundarias)

    estado_final = largura(estado_inicial)

    if estado_final:
        for linha in range(numero_rainhas):
            for coluna in range(numero_rainhas):
                print(estado_final.tabuleiro[linha][coluna], end=" ")
            print()
        print()
    else:
        print("Solucao nao encontrada!")


encontrar_solucao()
