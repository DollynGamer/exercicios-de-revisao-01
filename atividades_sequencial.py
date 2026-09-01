import math

# 01 Problema: Terreno

def terreno():
    largura = float(input("Digite a largura do terreno: "))
    comprimento = float(input("Digite o comprimento do terreno: "))
    valor = float(input("Digite o valor do metro quadrado: "))

    area = largura * comprimento
    preco = area * valor

    print(f"Area do terreno = {area:.2f}")
    print(f"Preco do terreno = {preco:.2f}")

# 02 Problema: Retangulo

def retangulo():
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))

    area = base * altura
    perimetro = 2 * (base + altura)
    diagonal = math.sqrt(base**2 + altura**2)

    print(f"Area = {area:.4f}")
    print(f"Perimetro = {perimetro:.4f}")
    print(f"Diagonal = {diagonal:.4f}")

# 03 Problema: Idade

def idade():
    print("Dados da Primeira Pessoa:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    print("\nDados da Segunda Pessoa:")
    nome2 = input("Digite o nome: ")
    idade2 = int(input("Digite a idade: "))

    media = (idade + idade2) / 2

    print(f"A idade media de {nome} e {nome2} eh de {media:.1f}")

# 04 Problema: Soma

def soma():
    valor1 = int(input("Digite o valor de X: "))
    valor2 = int(input("Digite o valor de Y: "))

    soma = valor1 + valor2

    print(f"Soma = {soma}")

# 05 Problema: Troco

def troco():
    preco = float(input("Preco unit. do produto: "))
    compra = int(input("Quantidade comprada: "))
    dinheiro = float(input("Dinheiro recebido: "))

    troco = dinheiro - (preco * compra)

    print(f"Troco: {troco:.2f}")

# 06 Problema: circulo

def circulo():
    raio = float(input("Digite o valor do raio do circulo: "))

    area = math.pi * raio**2

    print(f"Area = {area:.3f}")

# 07 Problema: Pagamento

def pagamento():
    nome = input("Digite seu nome: ")
    valor_hora = float(input("Digite o valor por hora: "))
    trabalhadas = int(input("Digite a quantidade trabalhada: "))

    pagamento = valor_hora * trabalhadas

    print(f"O pagamento para {nome} deve ser {pagamento:.2f}")

# 08 Problema: Consumo

def consumo():
    distancia = int(input("Distancia percorrida: "))
    combustivel = float(input("Combustivel gasto: "))

    media = distancia / combustivel

    print(f"Consumo medio = {media:.3f}")

# 09 Problema: Medidas

def medidas():
    medida1 = float(input("Digite a medida A: "))
    medida2 = float(input("Digite a medida B: "))
    medida3 = float(input("Digite a medida C: "))

    quadrado = medida1 ** 2
    triangulo = (medida1 * medida2) / 2
    trapezio = ((medida1 + medida2) * medida3) / 2

    print(f"Area do Quadrado: {quadrado:.4f}")
    print(f"Area do Triangulo: {triangulo:.4f}")
    print(f"Area do Trapezio: {trapezio:.4f}")