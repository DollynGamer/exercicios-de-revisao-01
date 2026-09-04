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