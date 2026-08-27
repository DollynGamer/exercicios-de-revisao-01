import math
from colorama import Fore, Back, Style, init

init()

print(Fore.RED + "-"*100 + Style.RESET_ALL)

# 01 Problema: Terreno

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))

area = largura * comprimento
preco = area * valor

print(f"Area do terreno = {area:.2f}")
print(f"Preco do terreno = {preco:.2f}")

print(Fore.RED + "-"*100 + Style.RESET_ALL)

# 02 Problema: Retangulo

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base**2 + altura**2)

print(f"Area = {area:.2f}")
print(f"Perimetro = {perimetro:.2f}")
print(f"Diagonal = {diagonal:.2f}")

print(Fore.RED + "-"*100 + Style.RESET_ALL)