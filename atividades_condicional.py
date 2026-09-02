import math

# 01 Problema: notas

def notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    resultado = nota1 + nota2

    print(f"Nota final: {resultado:.1f}")

    if resultado < 60.00:
        print("Reprovado.")
    else:
        print("Aprovado.")

# 02 Problema: baskara

def baskara():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Nao existe raizes reais")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Existe uma raize real: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print(f"X1: {x1:.4f}")
        print(f"X2: {x2:.4f}")

# 03 Problema: menor de tres

def menor_de_tres():
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))
    c = int(input("Terceiro valor: "))

    valores = [a, b, c]

    print(f"Menor: {min(valores)}")

# 04 Problema: operadora

def operadora():
    quantidade = int(input("Digite a quantidade de minutos: "))
    valor = 50.0

    if quantidade <= 100:
        print(f"Valor a pagar: R${valor:.2f}")
    else:
        for i in range(100, quantidade):
            valor = valor + 2
        print(f"Valor a pagar: R${valor:.2f}")

# 05 Problema: troco verificado

def troco_verificado():
    preco = float(input("Preco unit. do produto: "))
    compra = int(input("Quantidade comprada: "))
    dinheiro = float(input("Dinheiro recebido: "))
    
    troco = dinheiro - (preco * compra)

    if dinheiro >= (preco * compra):
        print(f"Troco: {troco:.2f}")
    else:
        troco = (preco * compra) - dinheiro
        print(f"Dinheiro insuficiente! faltam {troco:.2f}")

# 06 Problema: glicose

def glicose():
    glicose = float(input("Digite a medida da glicose: "))

    if glicose <= 100:
        print("Normal")
    elif glicose > 100 and glicose <= 140:
        print("Elevado")
    else:
        print("Diabetes")