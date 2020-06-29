import PySimpleGUI as sg


class DollarConversor:
    def __init__(self):
        sg.theme('LightBlue')
        self.dollar = 5.0
        self.valor = 'Dóllar: ${}'
        self.layout = [
            # Row
            [sg.Text('      Conversor de Real',
                     justification='center', font=('Arial', 24, 'bold'))
             ],
            # Row
            [sg.Text('Insira um valor R$:', justification='left',
                     font=('Arial', 16), size=(15, 1)),
             sg.Input('', enable_events=True, key='-R$-')
             ],
            # Row
            [sg.Text(self.valor, key='-VALOR-', size=(30, 1),
                     visible=False, text_color='black', font=('Arial', 15, 'bold'))],
        ]

    def iniciar(self):
        window = sg.Window('Conversor', layout=self.layout, size=(400, 120))

        while True:
            button, value = window.read()

            if button == sg.WIN_CLOSED:
                break

            try:
                if not (value['-R$-'][-1] in ('0123456789')):
                    window.find_element('-R$-').update(value['-R$-'][:-1])

            except IndexError:
                print('Nehum número digitado')

            quantia = value['-R$-']

            if self._é_numero(quantia):
                if float(quantia) > 9999999999:
                    window.find_element(
                        '-VALOR-').update('Dóllar:  Valor muito grande', text_color='red')
                else:
                    quantia_dollar = f'{float(quantia)/self.dollar:.2f}'
                    msg = self.valor.format(quantia_dollar)

                    window.find_element(
                        '-VALOR-').update(msg, visible=True, text_color='black')

            elif quantia == '':
                window.find_element('-VALOR-').update(
                    self.valor.format(0.00), visible=True)

    def _é_numero(self, n):
        try:
            n = float(n)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    conversor = DollarConversor()
    conversor.iniciar()
