temperatura = float(input("Digite a temperatura para conversão: "))

unidade_origem = input('''
Unidades => | C | F | K |
Unidade de Origem: ''').upper()

unidade_conversao = input('Unidade para conversão: ').upper

if unidade_origem == unidade_conversao:
    if unidade_origem == 'C':
        resultado_texto = f"As unidades são as mesmas. Temperatura: {temperatura:.2f}°C"
    elif unidade_origem == 'F':
        resultado_texto = f"As unidades são as mesmas. Temperatura: {temperatura:.2f}°F"
    elif unidade_origem == 'K':
        resultado_texto = f"As unidades são as mesmas. Temperatura: {temperatura:.2f}K"
    else:
        resultado_texto = f"Unidade de origem '{unidade_origem}' inválida. Use C, F ou K."
else:

    if unidade_origem == 'C':
        valor_origem_str = f"{temperatura:.2f}°C"
        if unidade_conversao == 'F':
            convertido = (temperatura * 9/5) + 32
            resultado_texto = f"{valor_origem_str} é igual a {convertido:.2f}°F"
        elif unidade_conversao == 'K':
            convertido = temperatura + 273.15
            resultado_texto = f"{valor_origem_str} é igual a {convertido:.2f}K"
        else:
            resultado_texto = f"Não é possível converter de Celsius para '{unidade_conversao}'. Verifique as unidades."

    elif unidade_origem == 'F':
        valor_origem_str = f"{temperatura:.2f}°F"
        if unidade_conversao == 'C':
            convertido = (temperatura - 32) * 5/9
            resultado_texto = f"{valor_origem_str} é igual a {convertido:.2f}°C"
        elif unidade_conversao == 'K':
            convertido = (temperatura - 32) * 5/9 + 273.15
            resultado_texto = f"{valor_origem_str} é igual a {convertido:.2f}K"
        else:
            resultado_texto = f"Não é possível converter de Fahrenheit para '{unidade_conversao}'. Verifique as unidades."

    elif unidade_origem == 'K':
        valor_origem_str = f"{temperatura:.2f}K"
        if unidade_conversao == 'C':
            convertido = temperatura - 273.15
            resultado_texto = f"{valor_origem_str} é igual a {convertido:.2f}°C"
        elif unidade_conversao == 'F':
            convertido = (temperatura - 273.15) * 9/5 + 32
            resultado_texto = f"{valor_origem_str} é igual a {convertido:.2f}°F"
        else:
            resultado_texto = f"Não é possível converter de Kelvin para '{unidade_conversao}'. Verifique as unidades."
    else:
        resultado_texto = f"Unidade de origem '{unidade_origem}' inválida. Use C, F ou K."

print(resultado_texto)
