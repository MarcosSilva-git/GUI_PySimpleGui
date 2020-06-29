import requests
import sys
import Dollar_conversor

# Pega o valor do dollar na internet
try:
    pagina = requests.get(
        'https://www.remessaonline.com.br/cotacao/cotacao-dolar')
    if pagina.status_code == 200:

        print(pagina.status_code)
        html = pagina.text
        valor = html.find(
            '<div class="style__Text-sc-27fg4f-2 ddwOcG">')
        tag_html = html[59403: 59463]

        dollar = tag_html[44:48].replace(',', '.')

        # Inicia a GUI
        conversor = Dollar_conversor.DollarConversor()
        conversor.dollar = float(dollar)

        with open('Dollar_Conversor/valor_do_dollar.txt', 'w') as file:
            file.write(dollar)
        conversor.iniciar()

    else:
        raise


except:
    print('Erro ao buscar o valor do dóllar')
    with open('Dollar_Conversor/valor_do_dollar.txt') as file:
        dollar = file.readline()

        conversor = Dollar_conversor.DollarConversor()
        conversor.dollar = float(dollar)
        conversor.iniciar()
