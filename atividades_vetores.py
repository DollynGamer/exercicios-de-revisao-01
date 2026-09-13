# 01 Problema: negativos

def negativos():
    maximo = int(input("Quantos numeros voce vai digitar?: "))
    valores = []

    for i in range(maximo):
        valores.append(int(input("Digite um numero: ")))


    print("Numeros negativos: ")
    for numero in valores:
        if numero < 0:
            print(numero)

# 02 Problema: soma vetor

def soma_vetor():
    maximo = int(input("Quantos numeros voce vai digitar?: "))
    valores = []

    for i in range(maximo):
        valores.append(float(input("Digite um numero: ")))

    media = sum(valores) / len(valores)

    print(f"Valores: {valores}")
    print(f"Soma: {sum(valores):.2f}")
    print(f"Media: {media:.2f}")

# 03 Problema: alturas

def alturas():
    maximo = int(input("Quantas pessoas serao digitadas?: "))
    pessoas = {}
    soma = 0
    menores = 0

    for i in range(maximo):
        print(f"Dados da {i + 1}a pessoa:")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))

        pessoas[f"pessoa{i + 1}"] = {
            "nome": nome,
            "idade": idade,
            "altura": altura
        }

    for chave, valor in pessoas.items():
        if valor["idade"] < 16:
            menores += 1

        soma += valor["altura"]

    media = soma / len(pessoas)
    percentual = (menores / len(pessoas)) * 100

    print(f"\nAltura media: {media:.2f}")
    print(f"Pessoas com menos de 16 anos: {percentual:.1f}%")
    for chave, valor in pessoas.items():
        if valor["idade"] < 16:
            print(valor["nome"])

# 04 Problema: numeros pares

def numeros_pares():
    maximo = int(input("Quantos numeros voce vai digitar?: "))
    pares = []
    qtd = 0

    for i in range(maximo):
        pares.append(int(input("Digite um numero: ")))

    print("\nNumeros pares:")
    for i in range(maximo):
        if pares[i] % 2 == 0:
                qtd += 1
                print(f"{pares[i]}", end=" ")
    print(f"\n\nQuantidade de pares = {qtd}")

# 05 Problema: maior posicao

def maior_posicao():
    maximo = int(input("Quantos numeros voce vai digitar?: "))
    valores = []
    maior = 0.0

    for i in range(maximo):
        valores.append(float(input("Digite um numero: ")))

    maior = max(valores)

    print(f"\nMaior valor = {maior}")
    print(f"Posicao do maior valor = {valores.index(maior)}")

# 06 Problema: soma vetores

def soma_vetores():
    maximo = int(input("Quantos valores vai ter cada vetor?: "))
    vetorA = []
    vetorB = []
    vetorC = []

    print("Digite os valores do vetor A:")
    for i in range(maximo):
        vetorA.append(int(input()))
    print("Digite os valores do vetor B:")
    for i in range(maximo):
        vetorB.append(int(input()))

    print("Vetor resultante:")
    for i in range(maximo):
        vetorC.append(vetorA[i] + vetorB[i])
        print(f"{vetorC[i]}")

# 07 Problema: abaixo da media

def abaixo_da_media():
    maximo = int(input("Quantos elementos vai ter o vetor?: "))
    valores = []

    for i in range(maximo):
        valores.append(float(input("Digite um numero: ")))

    media = sum(valores) / len(valores)

    print(f"\nMedia do vetor = {media:.3f}")
    print("Elementos abaixo da media:")
    for i in range(len(valores)):
        if valores[i] < media:
            print(valores[i])

# 08 Problema: media pares

def media_pares():
    maximo = int(input("Quantos elementos vai ter o vetor?: "))
    valores = []
    pares = []

    for i in range(maximo):
        valores.append(int(input("Digite um numero: ")))

    for i in range(maximo):
        if valores[i] % 2 == 0:
            pares.append(valores[i])

    if not pares:
        print("Nenhum numero par")
    else:
        media = sum(pares) / len(pares)
        print(f"Media dos pares = {media:.1f}")

# 09 Problema: mais velho

def mais_velho():
    maximo = int(input("Quantos elementos vai ter o vetor?: "))
    nomes = []
    idades = []

    for i in range(maximo):
        print(f"Dados da {i+1}a pessoa:")
        nomes.append(input("Nome: "))
        idades.append(int(input("Idade: ")))

    posicao = idades.index(max(idades))

    print(f"Pessoa mais velha: {nomes[posicao]}")

# 10 Problema: aprovados

def aprovados():
    maximo = int(input("Quantos alunos serao digitados?: "))
    alunos = {}
    aprovados = []

    for i in range(maximo):
        print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
        nome = input()
        nota1 = float(input())
        nota2 = float(input())

        alunos[f"aluno{i + 1}"] = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2
        }

    for chave, valor in alunos.items():
        media = (valor["nota1"] + valor["nota2"]) / 2

        if media >= 6.0:
            aprovados.append(valor["nome"])



    print(f"Alunos aprovados:")
    for aluno in aprovados:
        print(aluno)

# 11 Problema: dados pessoas

def dados_pessoas():
    maximo = int(input("Quantas pessoas serao digitadas?: "))
    pessoas = {}
    masculino = 0
    soma_mulheres = 0
    quantidade_mulheres = 0

    for i in range(maximo):
        altura = float(input(f"Altura da {i+1}a pessoa: "))
        genero = input(f"Genero da {i+1}a pessoa: ").lower()

        pessoas[altura] = genero

    for altura, genero in pessoas.items():
        if genero == "m":
            masculino += 1
        else:
            soma_mulheres += altura
            quantidade_mulheres += 1

    print(f"Menor altura = {min(pessoas)}")
    print(f"Maior altura = {max(pessoas)}")
    if quantidade_mulheres > 0:
        media = soma_mulheres / quantidade_mulheres
        print(f"Media das alturas das mulheres = {media:.2f}")
    print(f"Numero de homens = {masculino}")

# 12 Problema: comerciante

def comerciante():
    maximo = int(input("Serao digitados dados de quantos produtos?: "))
    produtos = {}
    lucro_abaixo = 0
    lucro_entre = 0
    lucro_acima = 0
    total_compra = 0
    total_venda = 0

    for i in range(maximo):
        print(f"Produto {i + 1}:")
        nome = input("Nome: ")
        compra = float(input("Preco de compra: "))
        venda = float(input("Preco de venda: "))

        produtos[f"produto{i + 1}"] = {
            "nome": nome,
            "compra": compra,
            "venda": venda
        }

    for chave, produto in produtos.items():
        compra = produto["compra"]
        venda = produto["venda"]

        lucro = venda - compra
        percentual = (lucro / compra) * 100

        total_compra += compra
        total_venda += venda

        if percentual < 10:
            lucro_abaixo += 1
        elif percentual <= 20:
            lucro_entre += 1
        else:
            lucro_acima += 1

    lucro_total = total_venda - total_compra

    print(f"Lucro abaixo de 10%: {lucro_abaixo}")
    print(f"Lucro entre 10% e 20%: {lucro_entre}")
    print(f"Lucro acima de 20%: {lucro_acima}")
    print(f"Valor total de compra: {total_compra:.2f}")
    print(f"Valor total de venda: {total_venda:.2f}")
    print(f"Lucro total: {lucro_total:.2f}")