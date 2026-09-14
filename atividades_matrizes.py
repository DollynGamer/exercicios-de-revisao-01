# 01 Problema: diagonal_negativos

def diagonal_negativos():
    maximo = int(input("Qual a ordem da matriz?: "))
    matriz = []
    qtd = 0

    for linha in range(maximo):
        matriz.append([])
        for coluna in range(maximo):
            valor = int(input(f"Elemento [{linha}][{coluna}]: "))
            matriz[linha].append(valor)
            if valor < 0:
                qtd += 1

    print("Diagonal principal:")
    for i in range(maximo):
        print(matriz[i][i], end=" ")
    print(f"\nQuantidade de negativos: {qtd}")

# 02 Problema: soma linhas

def soma_linhas():
    qtd_linhas = int(input("Qual a quantidade de linhas da matriz?: "))
    qtd_colunas = int(input("Qual a quantidade de colunas da matriz?: "))
    matriz = []
    soma = []

    for linhas in range(qtd_linhas):
        matriz.append([])
        for colunas in range(qtd_colunas):
            print(f"Digite os elementos da {linhas+1}a. linha: ")
            valor = float(input())
            matriz[linhas].append(valor)

    for linhas in range(qtd_linhas):
        soma.append(sum(matriz[linhas]))

    print("Vetor gerado:")
    print(*soma, sep="\n")

# 03 Problema: negativos matriz

def negativos_matriz():
    qtd_linhas = int(input("Qual a quantidade de linhas da matriz?: "))
    qtd_colunas = int(input("Qual a quantidade de colunas da matriz?: "))
    matriz = []

    for linhas in range(qtd_linhas):
        matriz.append([])
        for colunas in range(qtd_colunas):
            valor = int(input(f"Elemento [{linhas}][{colunas}]: "))
            matriz[linhas].append(valor)

    print("Valores negativos:")
    for linhas in range(qtd_linhas):
        for colunas in range(qtd_colunas):
            if matriz[linhas][colunas] < 0:
                    print(matriz[linhas][colunas])

# 04 Problema: cada linha

def cada_linha():
    maximo = int(input("Qual a ordem da matriz?: "))
    matriz = []

    for linha in range(maximo):
        matriz.append([])
        for coluna in range(maximo):
            valor = int(input(f"Elemento [{linha}][{coluna}]: "))
            matriz[linha].append(valor)

    print("Maior elemento de cada linha:")
    for linha in matriz:
        maior = max(linha)
        print(maior)

# 05 Problema: soma matrizes

def soma_matrizes():
    qtd_linhas = int(input("Quantas linhas vai ter cada matriz?: "))
    qtd_colunas = int(input("Quantas colunas vai ter cada matriz?: "))
    matrizA = []
    matrizB = []
    matrizC = []

    print("Digite os valores da matriz A:")
    for linha in range(qtd_linhas):
        matrizA.append([])
        for coluna in range(qtd_colunas):
            valor = int(input(f"Elemento [{linha}][{coluna}]: "))
            matrizA[linha].append(valor)
    print("Digite os valores da matriz B:")
    for linha in range(qtd_linhas):
        matrizB.append([])
        for coluna in range(qtd_colunas):
            valor = int(input(f"Elemento [{linha}][{coluna}]: "))
            matrizB[linha].append(valor)

    for linha in range(qtd_linhas):
        matrizC.append([])
        for coluna in range(qtd_colunas):
            valor = matrizA[linha][coluna] + matrizB[linha][coluna]
            matrizC[linha].append(valor)

    print("Matriz soma:")
    for linha in matrizC:
        print(*linha)

# 06 Problema: acima diagonal

def acima_diagonal():
    maximo = int(input("Qual a ordem da matriz?: "))
    matriz = []
    soma = 0

    for linha in range(maximo):
        matriz.append([])
        for coluna in range(maximo):
            valor = int(input(f"Elemento [{linha}][{coluna}]: "))
            matriz[linha].append(valor)

    for i in range(maximo):
        for j in range(i + 1, maximo):
            soma += matriz[i][j]

    print(f"Soma dos elementos acima da diagonal principal = {soma}")

# 07 Problema: matriz geral

def matriz_geral():
    maximo = int(input("Qual a ordem da matriz?: "))
    matriz = []
    soma = 0.0

    for linha in range(maximo):
        matriz.append([])
        for coluna in range(maximo):
            valor = float(input(f"Elemento [{linha}][{coluna}]: "))
            matriz[linha].append(valor)

    for linha in range(maximo):
        for coluna in range(maximo):
            if matriz[linha][coluna] >= 0:
                soma += matriz[linha][coluna]

    print(f"\nSoma dos positivos = {soma:.1f}\n")

    qual_linha = int(input("Escolha uma linha: "))
    print("Linha escolhida: ", *matriz[qual_linha], "\n")

    qual_coluna = int(input("Escolha uma coluna: "))
    print("Coluna escolhida: ", end=" ")
    for linha in range(maximo):
        print(matriz[linha][qual_coluna], end=" ")

    print("\n\nDiagonal principal: ", end=" ")
    for i in range(maximo):
        print(matriz[i][i], end=" ")

    for linha in range(maximo):
        for coluna in range(maximo):
            if matriz[linha][coluna] < 0:
                matriz[linha][coluna] = matriz[linha][coluna] ** 2

    print("\n\nMatriz alterada:")
    for linha in matriz:
        print(*linha)