nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5


def media(nota1, nota2, nota3):
    print(f'''
            Nota 1: {nota1}
            Nota 2: {nota2}
            Nota 3: {nota3}
            Média: {(nota1 + nota2 + nota3) / 3:.2f}
        ''')


media(nota_1, nota_2, nota_3)
