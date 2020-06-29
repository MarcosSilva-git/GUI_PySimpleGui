import menu
import registro

opcao = menu.tela_menu()

while True:
    if opcao == 1:
        opcao = registro.abrir_documento()

    elif opcao == 2:
        opcao = registro.registrar()

    elif opcao == 0:
        break

print(f'\033[36;1m {"-" * 15} {" Volte Sempre! "} {"-" * 15} \033[m')
