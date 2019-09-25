from copy import deepcopy


# Numero de rainhas que devem ser colocadas no tabuleiro
numero_rainhas = 8


class Estado:
    def __init__(self, tabuleiro, rainhas, colunas, linhas, diagonais_principais, diagonais_secundarias):
        # Matriz que ira representar o tabuleiro
        self.tabuleiro = tabuleiro

        # Numero de rainhas no tabuleiro
        self.rainhas = rainhas

        # Array utilizada para marcar as colunas que estao no alcance de uma rainha no tabuleiro
        self.colunas = colunas

        # Array utilizada para marcar as linhas que estao no alcance de uma rainha no tabuleiro
        self.linhas = linhas

        # Arrays utilizadas para marcar as diagonais que estao no alcance de uma rainha no tabuleiro,
        # o index eh calculado a partir da linha e coluna das posicoes das rainhas
        self.diagonais_principais = diagonais_principais
        self.diagonais_secundarias = diagonais_secundarias


def imprimir_tabuleiro(tabuleiro):
    for linha in range(numero_rainhas):
        for coluna in range(numero_rainhas):
            print(tabuleiro[linha][coluna], end=" ")
        print()
    print()


# Gera todos os filhos do estado atual e os adiciona a lista de abertos
def gerar_filhos(estado):
    abertos = []

    for coluna in range(numero_rainhas):
        if estado.colunas[coluna] != 1:
            for linha in range(numero_rainhas):
                # Verifica se eh possivel colocar uma rainha nessa posicao
                if (estado.diagonais_principais[linha - coluna + numero_rainhas - 1] != 1 and
                        estado.diagonais_secundarias[linha + coluna] != 1 and
                        estado.linhas[linha] != 1):

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


def busca_largura(estado_inicial):
    abertos = [estado_inicial]

    while len(abertos) != 0:
        estado = abertos[0]

        if estado.rainhas == numero_rainhas:
            return estado

        abertos = abertos + gerar_filhos(estado)
        abertos.pop(0)

    return None


def gerar_estado_inicial():
    tabuleiro = [[0 for linha in range(numero_rainhas)] for coluna in range(numero_rainhas)]
    rainhas = 0
    colunas = [0] * numero_rainhas
    linhas = [0] * numero_rainhas
    diagonais_principais = [0] * (numero_rainhas * 2 - 1)
    diagonais_secundarias = [0] * (numero_rainhas * 2)

    estado_inicial = Estado(tabuleiro, rainhas, colunas, linhas, diagonais_principais, diagonais_secundarias)
    return estado_inicial


def encontrar_solucao():
    estado_inicial = gerar_estado_inicial()
    estado_final = busca_largura(estado_inicial)

    if estado_final:
        print("Solucao encontrada:")
        imprimir_tabuleiro(estado_final.tabuleiro)
    else:
        print("Solucao nao encontrada!")


print("Problema das {}-rainhas".format(numero_rainhas))
print("Algoritmo de busca em largura")
print()
encontrar_solucao()
