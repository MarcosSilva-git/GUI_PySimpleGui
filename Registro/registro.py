import PySimpleGUI as sg


def abrir_documento():
    documento = ler_documento('r')

    if documento == 'não existe':
        print("\033[35mNão há ninguém registrado no momento\033[m")

    elif documento == 3:
        documento.close()
        return documento

    else:
        print('-'*26)
        print(f'{"pessoas.txt":^26}')
        print('-'*26)

        print(documento.read())
        print('\033[35mOperação Realizada com Sucesso!\033[m')

    return 0


def registrar():
    sg.theme('LightGrey3')

    layout = [[sg.T('Nome:'), sg.In(size=(30, 1), key='-NOME-')],
              [sg.T('Idade: '), sg.In(size=(30, 1),
                                      key='-IDADE-', enable_events=True)],
              [sg.Ok('   Salvar   ', key='-SALVA-')]]

    window = sg.Window('Registrar', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            return 0

        try:
            if values['-IDADE-'][-1] not in ('0123456789'):
                window.find_element('-IDADE-').update(values['-IDADE-'][:-1])

        except IndexError:
            pass

        if event == '-SALVA-':
            nome = values['-NOME-'].capitalize()

            if nome == '':
                sg.popup('Digite um nome')
                continue

            try:
                idade = int(values['-IDADE-'])
            except ValueError:
                sg.popup_ok('Digite uma idade válida.')
                continue

            else:
                documento = ler_documento('a')
                documento.write(f'{nome:<15}{idade} anos \n',)
                documento.close()

                window.find_element('-NOME-').update('')
                window.find_element('-IDADE-').update('')

                sg.Window('Cadastro Realizado', element_justification='center', layout=[
                    [sg.T('Cadastros Salvo', font=('Arial', 16, 'bold'))],
                    [sg.T()],
                    [sg.B('Cadastrar Outro Número', font=('Arial', 14))]]).read(close=True)


def ler_documento(mode='r'):

    try:
        file = open('Registro/pessoas.txt', mode)
        return file
    except KeyboardInterrupt:
        return 3
    except FileNotFoundError:
        return 'não existe'
