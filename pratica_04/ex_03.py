def verificar_forca_senha():

    print("""
Crie sua senha. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número
Digite 'sair' a qualquer momento para encerrar.
          """)

    while True:
        senha = input("Digite a senha desejada: ")

        if senha.lower() == 'sair':
            print("Criação de senha encerrada pelo usuário.")
            return False

        if len(senha) < 8:
            print("Senha muito curta. Deve ter pelo menos 8 caracteres.")
            continue

        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break

        if not tem_numero:
            print("Senha fraca. Deve conter pelo menos um número.")
            continue

        print("Senha forte registrada com sucesso!")
        return True


if __name__ == "__main__":
    if verificar_forca_senha():
        print("Programa encerrado.")
    else:
        print("Nenhuma senha forte foi definida.")
