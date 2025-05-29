def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta/100)


print(f'O valor da gorjeta é R$ {calcular_gorjeta(335, 12):.2f}')
