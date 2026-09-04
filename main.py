from atividades_sequencial import *
from atividades_condicional import *
from atividades_repeticao import *
from colorama import Fore, Back, Style, init

init()

menu = 0

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
    linhas(0)
    print("Bem vindo ao Menu inicial")
    print("Esse menu foi feito para você escolher/testar os exercicios de revisao")
    print("Leia com atencao para saber como navegar pelos menus, deixei tudo explicado para voce")
    print("\n Lista de Menus:")
    print("1 = Estrutura Sequencial (27/08/26)")
    print("2 = Estrutura Condicional (27/08/26)")
    print("3 = Estrutura de Repeticao (While e For) (27/08/26)")
    print("qualquer letra = Sair do programa")

    try:
        menu = int(input("Digite o numero para escolher qual menu voce quer acessar: "))
    except ValueError as e:
        print("Saindo...")
        linhas(1)
        break

    match menu:
        case 1:
            try:
                linhas(1)
                print("Atividades de Estrutura Sequencial")
                print("Escolha a atividade usando numeros de 1 a 9")
                print("Caso queira voltar para o menu inicial, use 0")
            
                opcao = input("Qual atividade você gostaria de ver?: ")
                
                match opcao:
                    case "0":
                        print("\nVoltando...")
                        menu = 0
                    case "1":
                        linhas(2)
                        terreno()
                    case "2":
                        linhas(2)
                        retangulo()
                    case "3":
                        linhas(2)
                        idade()
                    case "4":
                        linhas(2)
                        soma()
                    case "5":
                        linhas(2)
                        troco()
                    case "6":
                        linhas(2)
                        circulo()
                    case "7":
                        linhas(2)
                        pagamento()
                    case "8":
                        linhas(2)
                        consumo()
                    case "9":
                        linhas(2)
                        medidas()
                    case _:
                        print(Fore.RED + "\nNão existe!" + Style.RESET_ALL)
            except ValueError as e:
                print("Erro na digitação!")
        case 2:
            try:
                linhas(1)
                print("Atividades de Estrutura Condicional")
                print("Escolha a atividade usando numeros de 1 a 13")
                print("Caso queira voltar para o menu inicial, use 0")
            
                opcao = input("Qual atividade você gostaria de ver?: ")
            
                match opcao:
                    case "0":
                        print("\nVoltando...")
                        menu = 0
                    case "1":
                        linhas(2)
                        notas()
                    case "2":
                        linhas(2)
                        baskara()
                    case "3":
                        linhas(2)
                        menor_de_tres()
                    case "4":
                        linhas(2)
                        operadora()
                    case "5":
                        linhas(2)
                        troco_verificado()
                    case "6":
                        linhas(2)
                        glicose()
                    case "7":
                        linhas(2)
                        dardo()
                    case "8":
                        linhas(2)
                        temperatura()
                    case "9":
                        linhas(2)
                        lanchonete()
                    case "10":
                        linhas(2)
                        multiplos()
                    case "11":
                        linhas(2)
                        aumento()
                    case "12":
                        linhas(2)
                        tempo_de_jogo()
                    case "13":
                        linhas(2)
                        coordenadas()
                    case _:
                        print(Fore.RED + "\nNão existe!" + Style.RESET_ALL)
            except ValueError as e:
                print("Erro na digitação!")
        case 3:
            try:
                linhas(1)
                print("Atividades de Estrutura de Repetição (While e For)")
                print("Escolha a atividade usando numeros de 1 a 16")
                print("Caso queira voltar para o menu inicial, use 0")
                    
                opcao = input("Qual atividade você gostaria de ver?: ")
                    
                match opcao:
                    case "0":
                        print("\nVoltando...")
                        menu = 0
                    case "1":
                        linhas(2)
                        crescente()
                    case "2":
                        linhas(2)
                        media_idades()
                    case "3":
                        linhas(2)
                        senha_fixa()
                    case "4":
                        linhas(2)
                        quadrante()
                    case "5":
                        linhas(2)
                        validacao_de_nota()
                    case "6":
                        linhas(2)
                        combustivel()
                    case _:
                        print(Fore.RED + "\nNão existe!" + Style.RESET_ALL)
            except ValueError as e:
                print("Erro na digitação!")
        case _:
            print(Fore.RED + "\nNão existe!" + Style.RESET_ALL)