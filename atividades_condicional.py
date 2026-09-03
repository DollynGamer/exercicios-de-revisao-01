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

# 07 Problema: dardo

def dardo():
    lista = []

    print("Digite as tres distancias:")

    for i in range(3):
        lista.append(float(input()))

    print(f"Maior distancia = {max(lista):.2f}")

# 08 Problema: temperatura

def temperatura():
    tipo = input("Voce vai digitar a temperatura em qual escala? (C/F): ")

    match tipo:
        case "c":
            temp = float(input("Digite a temperatura em Celsius: "))
            temp = (temp * 9/5) + 32
            print(f"Temperatura equivalente em Fahrenheit: {temp:.2f}")
        case "f":
            temp = float(input("Digite a temperatura em Fahrenheit: "))
            temp = (temp - 32) * 5/9
            print(f"Temperatura equivalente em Celsius: {temp:.2f}")
        case _:
            print("escolha a temperatura (C/F)!")

# 09 Problema: lanchonete

def lanchonete():
    produtos = {
        1: 5.0,
        2: 3.5,
        3: 4.8,
        4: 8.9,
        5: 7.32
    }

    print("Bem vindo a lanchonete IDK:")
    print("Aqui vem a lista de Codigo do Produto e Preco do Produto:")
    for chave, valor in produtos.items():
        print(f"| {chave} | R${valor:.2f} |")
    comprado = int(input("Qual gostaria de comprar? (use o codigo): "))
    qtd = int(input("Quantos gostaria de comprar: "))

    valor = produtos[comprado] * qtd

    print(f"Valor a pagar: R${valor:.2f}")

# 10 Problema: multiplos

def multiplos():
    valor = []

    print("Digite dois numeros inteiros")
    for i in range(2):
        valor.append(int(input()))

    if valor[0] % valor[1] == 0:
        print("Sao multiplos")
    elif valor[1] % valor[0] == 0:
        print("Sao multiplos")
    else:
        print("Nao sao multiplos")

# 11 Problema: aumento

def aumento():
    salario = float(input("Digite o salario da pessoa: "))

    if salario <= 1000.0:
        aumento = salario * 0.20
        salario = salario + aumento

        print(f"Novo salario: R${salario:.2f} \nAumento: R${aumento:.2f} \nPorcentagem = 20%")
    elif salario > 1000.0 and salario <= 3000.0:
        aumento = salario * 0.15
        salario = salario + aumento
        
        print(f"Novo salario: R${salario:.2f} \nAumento: R${aumento:.2f} \nPorcentagem = 15%")
    elif salario > 3000.0 and salario <= 8000.0:
        aumento = salario * 0.10
        salario = salario + aumento
        
        print(f"Novo salario: R${salario:.2f} \nAumento: R${aumento:.2f} \nPorcentagem = 10%")
    else:
        aumento = salario * 0.5
        salario = salario + aumento
        
        print(f"Novo salario: R${salario:.2f} \nAumento: R${aumento:.2f} \nPorcentagem = 5%")

# 12 Problema: tempo de jogo

def tempo_de_jogo():
    hora_inicial = int(input("Hora inicial: "))
    hora_final = int(input("Hora final: "))

    duracao = (hora_final - hora_inicial) % 24

    if duracao == 0:
        duracao = 24
        print(f"O jogo durou {duracao} hora(s)")
    else:
        print(f"O jogo durou {duracao} hora(s)")

# 13 Problema: coordenadas

def coordenadas():
    x = float(input("Valor de X: "))
    y = float(input("Valor de Y: "))

    if x == 0 and y == 0:
        print("Origem")
    elif x > 0 and y > 0:
        print("Q1")
    elif x > 0 and y < 0:
        print("Q4")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x == 0 and y != 0:
        print("Eixo Y")
    else:
        print("Eixo X")