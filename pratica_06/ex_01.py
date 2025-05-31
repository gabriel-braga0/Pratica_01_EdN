import random
import string


def gerar_senha(comprimento):

    if comprimento < 4:
        print("A senha deve ter pelo menos 4 caracteres.")
        return None

    caracteres_minusculos = string.ascii_lowercase
    caracteres_maiusculos = string.ascii_uppercase
    digitos = string.digits
    caracteres_especiais = string.punctuation

    senha = [
        random.choice(caracteres_minusculos),
        random.choice(caracteres_maiusculos),
        random.choice(digitos),
        random.choice(caracteres_especiais)
    ]

    todos_os_caracteres = caracteres_minusculos + \
        caracteres_maiusculos + digitos + caracteres_especiais
    for i in range(comprimento - 4):
        senha.append(random.choice(todos_os_caracteres))

    random.shuffle(senha)

    return "".join(senha)


while True:
    try:
        comprimento_desejado = int(
            input("Digite a quantidade de caracteres da senha: "))
        if comprimento_desejado <= 0:
            print("Por favor, digite um número positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

senha_gerada = gerar_senha(comprimento_desejado)

if senha_gerada:
    print("Senha gerada:", senha_gerada)
