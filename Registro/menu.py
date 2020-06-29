import PySimpleGUI as sg


def tela_menu():
    sg.theme('LightGrey3')

    layout = [

        # Row 1
        [sg.Text('    Bem-Vindo Ao Programa', font=('courier', 20),
                 justification='center')],

        # Row 2
        [sg.Button(' Vizualizar Cadastros ', key='-VIZUALIZA-', font=('Arial', 16)),
         sg.Button('    Fazer Cadastros   ', key='-CADASTRA-', font=('Arial', 16))],
    ]

    window = sg.Window('Registradora', layout, text_justification='center')

    button, _ = window.read()

    window.close()

    if button == sg.WIN_CLOSED:
        return 0

    if button == '-VIZUALIZA-':
        return 1

    if button == '-CADASTRA-':
        return 2
