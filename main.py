from atividades_sequencial import *
from colorama import Fore, Back, Style, init

init()

def linhas(cor):
    match cor:
        case 0:
            print(Fore.WHITE + "-"*100 + Style.RESET_ALL)
        case 1:
            print(Fore.RED + "-"*100 + Style.RESET_ALL)
        case 2:
            print(Fore.GREEN + "-"*100 + Style.RESET_ALL)
        case _:
            print("Não existe essa cor!")

while(True):
    try:
        linhas(1)
        print("Atividades de Estrutura Sequencial")
        print("Escolha a atividade usando numeros de 1 a 9")

        opcao = int(input("Qual atividade você gostaria de ver?: "))

        match opcao:
            case 0:
                print("\nSaindo...")
                linhas(1)
                break
            case 1:
                linhas(2)
                terreno()
            case 2:
                linhas(2)
                retangulo()
            case 3:
                linhas(2)
                idade()
            case 4:
                linhas(2)
                soma()
            case 5:
                linhas(2)
                troco()
            case 6:
                linhas(2)
                circulo()
            case 7:
                linhas(2)
                pagamento()
            case 8:
                linhas(2)
                consumo()
            case 9:
                linhas(2)
                medidas()
            case _:
                print(Fore.RED + "\nNão existe!" + Style.RESET_ALL)
    except ValueError as e:
        print("Erro na digitação!")