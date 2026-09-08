import math

# 01 Problema: crescente

def crescente():
    while True:
        print("Digite dois numeros:")
        x = int(input())
        y = int(input())

        if x > y:
            print("Decrescente!")
        elif y > x:
            print("Crescente!")
        else:
            break

# 02 Problema: media idades

def media_idades():
    valor = []
    print("Digite as idades:")
    while True:
        idade = int(input())

        if idade < 0:
            break

        valor.append(idade)

    media = sum(valor) / len(valor)

    print(f"Media = {media:.2f}")

# 03 Problema: senha fixa

def senha_fixa():
    senha = 2002
    valor = int(input("Digite a senha: "))

    while True:
        if valor != senha:
            valor = int(input("Senha Invalida! Tente novamente: "))
        else:
            print("Acesso permitido!")
            break

# 04 Problema: quadrante

def quadrante():
    while True:
        x = float(input("Valor de X: "))
        y = float(input("Valor de Y: "))

        if x > 0 and y > 0:
            print("Quadrante Q1")
        elif x > 0 and y < 0:
            print("Quadrante Q4")
        elif x < 0 and y > 0:
            print("Quadrante Q2")
        elif x < 0 and y < 0:
            print("Quadrante Q3")
        else:
            break

# 05 Problema: validacao de nota

def validacao_de_nota():
    while True:
        try:
            nota1 = float(input("Digite a primeira nota: "))
            if nota1 >= 0 and nota1 <= 10:
                break
            else:
                print("Valor invalido! Tente novamente!")
        except ValueError as e:
            print("Valor invalido! Tente novamente!")

    while True:
        try:
            nota2 = float(input("Digite a segunda nota: "))
            if nota2 >= 0 and nota2 <= 10:
                break
            else:
                print("Valor invalido! Tente novamente!")
        except ValueError as e:
            print("Valor invalido! Tente novamente!")
            

    media = (nota1 + nota2) / 2

    print(f"Media = {media:.2f}")

# 06 Problema: combustivel

def combustivel():
    combustivel = {
        "Alcool": 0,
        "Gasolina": 0,
        "Diesel": 0
    }

    while True:
        try:
            valor = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

            match valor:
                case 1:
                    combustivel["Alcool"] += 1
                case 2:
                    combustivel["Gasolina"] += 1
                case 3:
                    combustivel["Diesel"] += 1
                case 4:
                    print("Muito obrigado!")
                    for chave, valor in combustivel.items():
                        print(f"{chave}: {valor}")
                    break
                case _:
                    print("Nao existe esse codigo!")
        except ValueError as e:
                print("Use apenas numeros!")

# 07 Problema: pares consecutivos

def pares_consecutivos():
    pares = []

    while True:
        valor = int(input("Digite um numero inteiro: "))

        if valor == 0:
            break
        elif valor % 2 == 0:
            pares.append(valor)
            for i in range(4):
                pares.append(pares[-1] + 2)
        else:
            pares.append(valor + 1)
            for i in range(4):
                pares.append(pares[-1] + 2)

        valor = sum(pares)

        print(f"Soma: {valor}")
        #print(f"Lista: {pares}") #debug da lista
        pares.clear()

# 08 Problema: tabuada

def tabuada():
    valor = int(input("Deseja a tabuada para qual valor?: "))

    for i in range(1, 11):
        resposta = valor * i
        print(f"{valor} X {i} = {resposta}")

# 09 Problema: soma impares

def soma_impares():
    print("Digite dois numeros: ")
    valor_min = int(input())
    valor_max = int(input())

    impares = []

    if valor_min > valor_max:
        temp = valor_min
        valor_min = valor_max
        valor_max = temp

    for i in range(valor_min, valor_max):
        if i % 2 != 0:
            impares.append(i)

    print(f"Soma dos impares: {sum(impares)}")
    #print(f"Lista: {impares}") #debug da lista

# 10 Problema: sequencia impares

def sequencia_impares():
    valor = int(input("Digite o valor de X: "))

    for i in range(valor):
        if i % 2 != 0:
            print(i)

# 11 Problema: dentro fora

def dentro_fora():
    maximo = int(input("Quantos numeros voce vai digitar?: "))
    valores = []
    fora = 0
    dentro = 0

    for i in range(maximo):
        valores.append(int(input("Digite um numero: ")))

        if valores[i] >= 10 and valores[i] <= 20:
            dentro += 1
        else:
            fora += 1

    print(f"{dentro} Dentro")
    print(f"{fora} Fora")

# 12 Problema: par impar

def par_impar():
    maximo = int(input("Quantos numeros voce vai digitar?: "))

    for i in range(maximo):
        valor = int(input("Digite um numero: "))

        if valor % 2 == 0 and valor < 0:
            print("Par negativo")
        elif valor % 2 != 0 and valor < 0:
            print("Impar negativo")
        elif valor == 0:
            print("Nulo")
        if valor % 2 == 0 and valor > 0:
            print("Par positivo")
        elif valor % 2 != 0 and valor > 0:
            print("Impar positivo")

# 13 Problema: media ponderada

def media_ponderada():
    maximo = int(input("Quantos casos voce vai digitar?: "))
    valores = []
    media = 0.0

    for i in range(maximo):
        print("Digite tres numeros:")
        for i in range(3):
            valores.append(float(input()))

        media = (valores[0] * 2 + valores[1] * 3 + valores[2] * 5) / 10
        valores.clear()

        print(f"Media: {media:.1f}")

# 14 Problema: divisao

def divisao():
    maximo = int(input("Quantos casos voce vai digitar?: "))

    for i in range(maximo):
        numerador = int(input("Entre com o numerador: "))
        denominador = int(input("Entre com denominador "))

        if denominador == 0:
            print("Divisao impossivel!")
        else:
            resposta = numerador / denominador

        print(f"Divisao: {resposta}")

# 15 Problema: fatorial

def fatorial():
    valor = int(input("Digite o valor de N: "))

    if valor > 0 and valor <= 15:
        fatorial = 1

        for i in range(1, valor + 1):
            fatorial *= i

        print(f"Fatorial = {fatorial}")
    else:
        print("Valor invalido!")

# 16 Problema: experiencias

def experiencias():
    maximo = int(input("Quantos casos de teste serao digitados?: "))
    cobaia = {
        "Rato": 0,
        "Sapo": 0,
        "Coelho": 0
    }

    for i in range(maximo):
        qtd = int(input("Quantidade de cobais: "))
        tipo = input("Tipo de cobaia (R/S/C): ")

        match tipo:
            case "r":
                cobaia["Rato"] += qtd
            case "s":
                cobaia["Sapo"] += qtd
            case "c":
                cobaia["Coelho"] += qtd
            case _:
                print("Nao existe esse tipo!")

    total = sum(cobaia.values())

    print("Relatorio final:")
    print(f"Total: {total} cobaias")
    print(f"Total de Ratos: {cobaia['Rato']}")
    print(f"Total de Sapos: {cobaia['Sapo']}")
    print(f"Total de Coelho: {cobaia['Coelho']}")
    for chave, valor in cobaia.items():
        percentual = (valor / total) * 100
        print(f"{chave}: {percentual:.2f}%")
