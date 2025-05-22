valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15


def conversor(valor, taxa):
    return valor/taxa


print(f'''
      Valor em reais: R$ {valor_reais:.2f}
      Valor em dolares: {conversor(valor_reais, taxa_dolar):.2f}
      Valor em euros: {conversor(valor_reais, taxa_euro):.2f}
    ''')
