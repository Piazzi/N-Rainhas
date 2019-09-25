# Numero de rainhas que devem ser colocadas no tabuleiro
numero_rainhas = 8

# Array utilizada para marcar as linhas que estao no alcance de uma rainha no tabuleiro
linhas = [0] * numero_rainhas

# Arrays utilizadas para marcar as diagonais que estao no alcance de uma rainha no tabuleiro,
# o index eh calculado a partir da linha e coluna das posicoes das rainhas
diagonais_principais = [0] * (numero_rainhas * 2 - 1)
diagonais_secundarias = [0] * (numero_rainhas * 2)


def imprimir_tabuleiro(tabuleiro):
    for linha in range(numero_rainhas):
        for coluna in range(numero_rainhas):
            print(tabuleiro[linha][coluna], end=" ")
        print()
    print()


# Marca ou desmarca posicoes que estao no alcance de alguma rainha no tabuleiro
def marcar_posicoes_no_alcance(tabuleiro, linha, coluna, no_alcance):
    tabuleiro[linha][coluna] = no_alcance
    linhas[linha] = no_alcance
    diagonais_principais[linha - coluna + numero_rainhas - 1] = no_alcance
    diagonais_secundarias[linha + coluna] = no_alcance


def backtracking(tabuleiro, coluna, nivel):
    # A solucao eh encontrada se as n rainhas ocuparem as n colunas
    # estando de acordo com as regras do problema
    if coluna == numero_rainhas:
        return True

    for linha in range(numero_rainhas):
        # Verifica se eh possivel colocar uma rainha nessa posicao
        if ((diagonais_principais[linha - coluna + numero_rainhas - 1] != 1 and
             diagonais_secundarias[linha + coluna] != 1) and
                linhas[linha] != 1):

            marcar_posicoes_no_alcance(tabuleiro, linha, coluna, 1)

            if backtracking(tabuleiro, coluna + 1, nivel):
                return True

            marcar_posicoes_no_alcance(tabuleiro, linha, coluna, 0)

    return False


def encontrar_solucao():
    # Cria matriz que ira representar o tabuleiro do problema
    tabuleiro = [[0 for linha in range(numero_rainhas)] for coluna in range(numero_rainhas)]

    if backtracking(tabuleiro, 0, 0):
        print("Solucao encontrada:")
        imprimir_tabuleiro(tabuleiro)
    else:
        print("Nao existe solucao!")


print("Problema das {}-rainhas".format(numero_rainhas))
print("Algoritmo de backtracking")
print()

encontrar_solucao()
